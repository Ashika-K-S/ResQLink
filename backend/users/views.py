from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import api_view, permission_classes

from .models import User
from .serializers import UserRegistrationSerializer

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_decode

class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        return data


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")

            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            django_logout(request)

            return Response(
                {"message": "Logged out successfully"},
                status=status.HTTP_200_OK
            )

        except Exception:
            return Response(
                {"error": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST
            )



def google_login_callback(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("http://localhost:3000/login")


    refresh = RefreshToken.for_user(user)

    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

 
    role_to_send = user.role if user.is_role_set else ""

    return redirect(
        f"http://localhost:3000/social-login-success"
        f"?access={access_token}"
        f"&refresh={refresh_token}"
        f"&role={role_to_send}"
    )

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def set_role(request):
    user = request.user
    role = request.data.get("role")

    if role not in ["citizen", "volunteer", "authority"]:
        return Response({"error": "Invalid role"}, status=400)

    user.role = role
    user.is_role_set = True
    user.save()

    return Response({"message": "Role updated"})



@api_view(["POST"])
def forgot_password(request):
    email = request.data.get("email")

    try:
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"error": "User not found"}, status=404)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        reset_url = f"http://localhost:3000/reset-password/{uid}/{token}/"

        send_mail(
            subject="Reset your password",
            message=f"Click here to reset password: {reset_url}",
            from_email=getattr(settings, 'EMAIL_HOST_USER', 'noreply@resqlink.com'),
            recipient_list=[email],
        )

        return Response({"message": "Reset link sent"})

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    

@api_view(["POST"])
def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid token"}, status=400)

        password = request.data.get("password")
        from django.contrib.auth.password_validation import validate_password
        try:
            validate_password(password, user)
        except Exception as ve:
            return Response({"error": list(ve.messages)}, status=400)

        user.set_password(password)
        user.save()

        return Response({"message": "Password reset successful"})

    except Exception:
        return Response({"error": "Something went wrong"}, status=400)