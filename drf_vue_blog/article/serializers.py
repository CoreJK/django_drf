from rest_framework import serializers
from article.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at'
        ]