
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


class CommentSerializer(serializers.Serializer):
    # article = serializers.SerializerMethodField()
    article = serializers.ChoiceField(Article.objects.filter(status='publish'))
    name = serializers.CharField(max_length=20, default='Anonymous Users')
    comment = serializers.CharField(max_length=500)

    class Meta:
        model = Comment
        fields = ('name', 'article', 'comment')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class Comment1Serializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name')
    article_name = serializers.CharField(source='article.title')

    class Meta:
        model = Comment
        fields = ['user_name', 'article_name', 'comment']
