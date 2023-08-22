
from django.urls import path
from .views import UserRegistrationView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
]