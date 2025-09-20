from django.urls import path
from .views import CustomUserView, LoginView, LogoutView, UserRegistrationView

urlpatterns = [
    path('user/', CustomUserView.as_view(), name='user'),
    path('register/', UserRegistrationView.as_view(), name="register-user"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("logout/", LogoutView.as_view(), name="user-logout"),
]