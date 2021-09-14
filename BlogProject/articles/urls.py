from django.urls import path
from articles.views import ArticleCreateApi

urlpatterns = [
    path('create/', ArticleCreateApi.as_view()),
]
