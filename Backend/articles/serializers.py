from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title_en', 'content_en', 'title_so', 'content_so', 'created_at', 'updated_at']