from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404

from article.models import Article
from article.serializers import ArticleDetailSerializer

# Create your views here.

class ArticleDetail(APIView):
    """文章详情视图"""
    
    def get_object(self, pk):
        """获取单个文章对象"""
        try:
            return Article.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        """获取接口"""
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """更新文章接口"""
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """删除文章接口"""
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)