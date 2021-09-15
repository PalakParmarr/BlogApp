from rest_framework import generics
from articles.serializer import ArticleCreateSerializer, ArticleSerializer, CategoriesSerializer
from articles.models import Article, Categories
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import filters
from .pagination import CustomPagination
# Create your views here.


class ArticleCreateApi(LoginRequiredMixin, generics.CreateAPIView):
    """ api view for reate atricle"""
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserArticleListApi(LoginRequiredMixin, generics.ListAPIView):
    """This view return a list of all the articles created by the currently authenticated user."""
    serializer_class = ArticleCreateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    pagination_class = CustomPagination

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleUpdateApi(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    """user can update thier articles"""
    serializer_class = ArticleCreateSerializer

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDeleteApi(LoginRequiredMixin, generics.DestroyAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()


class GeneralArticleListApi(generics.ListAPIView):
    """general article list"""
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__first_name']
    ordering_fields = ['category', 'title']

    def get_queryset(self):
        return Article.objects.filter(status="publish")

# ----- categoires view-api ---------


class CategoriesListApi(generics.ListAPIView):
    serializer_class = CategoriesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']

    def get_queryset(self):
        return Categories.objects.all()


class CategoryArticleList(generics.ListAPIView):
    """ general list api view to get categories wise articles"""
    serializer_class = ArticleSerializer

    def get_queryset(self):
        category = self.kwargs['pk']
        return Article.objects.filter(category__pk=category, status='publish')
