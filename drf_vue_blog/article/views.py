from rest_framework import generics

from article.models import Article
from article.permissions import IsAdminUserOrReadOnly
from article.serializers import ArticleListSerializer, ArticleDetailSerializer

# Create your views here.

class ArticleList(generics.ListCreateAPIView):
    """获取所有文章视图"""
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """文章相关的操作视图"""
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    
    