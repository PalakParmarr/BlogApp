from django.urls import path
from articles.views import ArticleCreateApi, UserArticleListApi, GeneralArticleListApi, ArticleUpdateApi

urlpatterns = [
    path('create/', ArticleCreateApi.as_view()),
    path('list/', UserArticleListApi.as_view()),
    path('', GeneralArticleListApi.as_view()),
    path('<int:pk>/', ArticleUpdateApi.as_view()),

]
