from .models import BlogsComment
from .serializers import BlogsCommentSerializer
from rest_framework import viewsets

class BlogsCommentView(viewsets.ModelViewSet):
    queryset = BlogsComment.objects.all()
    serializer_class = BlogsCommentSerializer   
