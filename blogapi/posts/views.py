from rest_framework import generics
from .permissions import IsAuthorOrReadyOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadyOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
