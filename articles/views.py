from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from articles.models import Article
from rest_framework.views import APIView
from articles.seriallzers import ArticleSerializer



class articleAPI(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class article_detailAPI(APIView):
    
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id = article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id = article_id)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id = article_id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)