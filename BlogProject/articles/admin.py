from django.contrib import admin
from articles.models import Article, Comment, Categories
# Register your models here.

admin.site.register(Categories)
admin.site.register(Article)
admin.site.register(Comment)
