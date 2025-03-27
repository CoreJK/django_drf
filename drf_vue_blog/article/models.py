from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    # 作者
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    # 标题
    title = models.CharField(max_length=100)
    # 正文
    content = models.TextField()    
    # 创建时间
    created_at = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title