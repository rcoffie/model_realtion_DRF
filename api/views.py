from django.shortcuts import render
from rest_framework import generics
from api.serializer import UserSerializer, PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from api.models import Post, Comment
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
