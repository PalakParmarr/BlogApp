from rest_framework import serializers
from articles.models import Article, Comment, Categories


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'status', 'image']
