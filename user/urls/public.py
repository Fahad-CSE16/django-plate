from django.urls import path
from user.views.public import (
    registration, 
    login, 
    refreshed_token
)
app_name = 'public'

urlpatterns = [
    path('/register', registration, name='user-registration-api'),
    path('/login', login, name='user-login-api'),
    path('/refresh_token', refreshed_token, name='user-token-refresh-api'),
]


