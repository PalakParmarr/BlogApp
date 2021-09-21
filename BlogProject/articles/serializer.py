from rest_framework import serializers
from articles.models import Article, Categories, Comment

# articles serializers


class ArticleCreateSerializer(serializers.ModelSerializer):
    """for create article"""
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

# comment serializer


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.filter(status='publish'))

    class Meta:
        model = Comment
        fields = ('name', 'article', 'comment')


class Comment1Serializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name')
    article_name = serializers.CharField(source='article.title')

    class Meta:
        model = Comment
        fields = ['user_name', 'article_name', 'comment']
