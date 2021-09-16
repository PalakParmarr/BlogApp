from rest_framework import serializers
from articles.models import Article, Categories, Comment, STATUS

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

# comment serializer


class CommentSerializer(serializers.ModelSerializer):
    #article_name = serializers.CharField(source='article.title')
    article = serializers.ChoiceField(Article.objects.filter(status='publish'))

    class Meta:
        model = Comment
        fields = ['article', 'comment']

    # def get_article(self, obj):
    #     article = Article.objects.filter(status='publish')
    #     return article


class Comment1Serializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name')
    article_name = serializers.CharField(source='article.title')

    class Meta:
        model = Comment
        fields = ['user_name', 'article_name', 'comment']