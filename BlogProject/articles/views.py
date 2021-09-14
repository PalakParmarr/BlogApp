from rest_framework import generics
from articles.serializer import ArticleSerializer
from articles.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ArticleCreateApi(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    