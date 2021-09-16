from django.urls import path
from articles.views import ArticleCreateApi, UserArticleListApi, GeneralArticleListApi, ArticleDeleteApi, ArticleUpdateApi, CategoriesListApi, CategoryArticleList

urlpatterns = [
    path('create/', ArticleCreateApi.as_view()),
    path('list/', UserArticleListApi.as_view()),
    path('list/<int:pk>/', ArticleUpdateApi.as_view()),
    path('list<int:pk>/delete', ArticleDeleteApi.as_view()),
    path('', GeneralArticleListApi.as_view()),
    path('categories/', CategoriesListApi.as_view()),
    path('categories/<int:pk>/', CategoryArticleList.as_view()),
]
