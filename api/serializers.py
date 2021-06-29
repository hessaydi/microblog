from rest_framework import serializers
from authentication.models import User
from .models import (
    Post, Hashtag
)

# class HashtagSerializer(serializers.ModelSerializer):
class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']

class PostListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    hashtags = HashtagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'hashtags']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'hashtags']

class HashtagListSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Hashtag
        fields = ['id', 'name' , 'posts']

class UserSerializer(serializers.ModelSerializer):
    favorites = HashtagSerializer(many=True, read_only=False, required=False)
    # favorates = serializers.ReadOnlyField(source='voted_by.username')
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'favorites']
