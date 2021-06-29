from django.urls import path
from rest_framework.routers import DefaultRouter
from authentication.views import UserListViewSet
from .views import (
    PostViewSet, HashtagPostList, FiveCommonHashtagList, UserDetails, 
    # UserViewSet, 
    HashtagPostsList
)

app_name='blog_api'
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserListViewSet, basename='users')
# router.register('user/details', UserViewSet, basename='user')
# user_detail = UserViewSet.as_view({'get': 'retrieve'})
# update_user_detail = UserViewSet.as_view({'put': 'update'})

custom_urlpatterns = [
    path('hashtags/posts/', HashtagPostsList.as_view(), name='hashtags_posts'),
    # path('user/details/<int:pk>', user_detail, name='user_details'),
    # path('user/update/<int:pk>', update_user_detail, name='user_details'),
    path('hashtags/common/', FiveCommonHashtagList.as_view(), name='common_hashtags'),
    path('post/<int:hashtag_id>/', HashtagPostList.as_view(), name='hashtags'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
