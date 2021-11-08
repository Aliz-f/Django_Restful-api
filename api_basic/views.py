from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import ArticleSerializers
from .models import Article

# Create your views here.

@csrf_exempt
def article_list(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializers(article, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)


@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk = pk)
    except Article.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == "GET":
        serializer = ArticleSerializers(article)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializers(article, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
    
    elif request.method == "DELET":
        article.delete()
        return HttpResponse(status = 204)