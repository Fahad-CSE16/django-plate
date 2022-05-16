from django.urls import path
from user.views.admin import AdminUserListAPIView

app_name = 'admin'

urlpatterns = [
    path('users', AdminUserListAPIView.as_view(), name='admin-user-list'),
]
