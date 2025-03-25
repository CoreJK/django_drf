from rest_framework import generics

from article.models import Article
from article.serializers import ArticleDetailSerializer

# Create your views here.

class ArticleList(generics.ListCreateAPIView):
    """获取所有文章视图"""
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """文章相关的操作视图"""
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    
    
    