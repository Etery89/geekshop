from django.urls import path

from adminapp.views import index, admin_users_recovery
from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
    path('admin-users-recovery/<int:user_id>/', admin_users_recovery, name='admin_users_recovery'),
]