from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import CustomTokenView
from users.views import UserRegistrationView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('emergency.urls')),
    path('api/users/', include('users.urls')),
    path('api/token/', CustomTokenView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('api/users/register/', UserRegistrationView.as_view())
    
    
]
