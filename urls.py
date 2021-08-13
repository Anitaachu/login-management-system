from django.urls import path, include
from .main import RegisterAPI, LoginAPI, VerifyEmailAPI, SetNewPasswordAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
#from knox import views as knox_views
 
urlpatterns = [
    path('main/auth/register/', RegisterAPI.as_view(), name='register'), 
    path('main/auth/login/', LoginAPI.as_view(), name='login'),
    #path('main/auth/user', UserAPI.as_view(), name='user'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path('main/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('main/auth/email-verify/', VerifyEmailAPI.as_view(), name='email-verify'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),    
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]