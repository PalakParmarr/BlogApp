from rest_framework import serializers
from articles.models import Article, Categories

# articles serializers


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'category', 'status', 'image']


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.first_name')

    class Meta:
        model = Article
        fields = ['title', 'author_name', 'content', 'category', 'image']

# category serializer


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['title', 'image']
