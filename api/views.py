from django.db.models import Count
from rest_framework import status
from authentication.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import (
    PermissionDenied
)
from rest_framework.permissions import IsAuthenticated
import re
from .models import (
    Post, Hashtag
)
from .serializers import (
    HashtagSerializer, UserSerializer,
    PostListSerializer, HashtagListSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # queryset = Post.objects.all().filter(owner=self.request.user)
        queryset = Post.objects.all().filter(is_deleted=False)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create posts")
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post  = Post.objects.get(pk=self.kwargs["pk"])
        post.is_deleted = True
        post.save()
        if request.user.is_anonymous:
            raise PermissionDenied(
                "You have no permissions to delete this post")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.user.is_anonymous:
            raise PermissionDenied(
                "You have no permissions to edit this post")
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        print(serializer)
        serializer.save(owner=self.request.user)

class HashtagsList(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Hashtag.objects.get(pk=self.kwargs.get("pk"))
        return queryset
    serializer_class = HashtagListSerializer

class HashtagPostList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        if 'hashtag_id' in self.kwargs:
            hashtag = self.kwargs.get("hashtag_id")
            queryset = Post.objects.filter(hashtags__id=hashtag)
        return queryset
    serializer_class = PostListSerializer
    
class FiveCommonHashtagList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Hashtag.objects.annotate(num_views=Count('posts')).order_by('-num_views','-updated_at')[:5]
        return queryset
    serializer_class = HashtagSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = User.objects.get(pk=self.kwargs['pk'])
        print(queryset)
        return queryset
    serializer_class = UserSerializer

class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def retrieve(self, request, pk=None):
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
class HashtagPostsList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Hashtag.objects.filter(users=self.request.user)
        return queryset
    serializer_class = HashtagListSerializer