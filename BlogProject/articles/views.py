from rest_framework import generics
from articles.serializer import ArticleCreateSerializer, Comment1Serializer, ArticleSerializer, CategoriesSerializer, CommentSerializer
from articles.models import Article, Categories, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ArticleCreateApi(LoginRequiredMixin, generics.CreateAPIView):
    """ api view for reate atricle"""
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class UserArticleListApi(LoginRequiredMixin, generics.ListAPIView):
#     """This view return a list of all the articles created by the currently authenticated user."""
#     serializer_class = ArticleCreateSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['title']
#     ordering_fields = ['title']
#     pagination_class = CustomPagination

#     def get_queryset(self):
#         return Article.objects.filter(author=self.request.user)

class UserArticleListApi(APIView):
    """This view return a list of all the articles created by the currently authenticated user."""
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)


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

# ----- comment


class CommentCreateApi(generics.CreateAPIView):
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()


# class CommentCreateApi(APIView):
#     def get(self, request, format=None):
#         comment = Comment.objects.all()
#         print(comment)
#         data = serializers.serialize('json', comment, fields=('name','article','comment'))
#         return Response(data)

#     def post(self, request, format=None):
#         serializer = CommentSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


class CommentListApi(generics.ListAPIView):
    serializer_class = Comment1Serializer

    def get_queryset(self):
        return Comment.objects.all()
