from django.urls import path
from .views import UserRegistrationView
from .views import LogoutView   
from .views import google_login_callback
from .views import set_role
from .views import forgot_password, reset_password

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
     path('logout/', LogoutView.as_view()),
     path("google/callback/", google_login_callback),
     path("set-role/", set_role),
     path('forgot-password/', forgot_password),
     path('reset-password/<uidb64>/<token>/', reset_password),

]
