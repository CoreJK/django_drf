from rest_framework import serializers

from article.models import Article
from user_info.serializers import UserDescSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    
    author = UserDescSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at'
        ]
        # 嵌套序列化器已经设置了只读，所以这个就不需要了
        # read_only_fields = ['author']

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'