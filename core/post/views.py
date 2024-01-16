from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .serializers import CreateUpdatePostSerializer,ListRetrivePostSerializer
from post.models import Post
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrAdmin


class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreateUpdatePostSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class ListPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ListRetrivePostSerializer

class DetailPost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = ListRetrivePostSerializer

class UpdatePost(UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthorOrAdmin]
    serializer_class = CreateUpdatePostSerializer
class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthorOrAdmin]
