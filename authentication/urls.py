# from django.conf.urls import url
from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserListViewSet

app_name = 'authentication'

urlpatterns = [
    path('users/', UserListViewSet.as_view({'get': 'list'}), name='user_list'),
    path('users/register/', RegistrationAPIView.as_view(), name='register'),
    path('users/login/',LoginAPIView.as_view(), name='login'),
]