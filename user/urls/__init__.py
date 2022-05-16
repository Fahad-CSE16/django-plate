from django.urls import path, include

app_name = 'public.users'

urlpatterns = [
    path('public', include('user.urls.public'), name='public.api'),
    path('admin/', include('user.urls.admin'), name='admin.api'),
    path('user/', include('user.urls.user'), name='user.api')
]
