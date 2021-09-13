from django.db import models
from accounts.models import User

# Create your models here.
STATUS = (
    ("draft", "draft"),
    ("publish", "publish"),
)


class Categories(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField()


class Article(models.Model):
    """article model for article to create, update, list"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Categories)
    status = models.CharField(choices=STATUS, max_length=20)
    image = models.ImageField()
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now_add=True, null=True)


class Comment(models.Model):
    """comment model to comment a message on article"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now_add=True, null=True)
