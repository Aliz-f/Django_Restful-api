from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response

from rest_framework import serializers #***Method 1
from rest_framework.parsers import JSONParser #***Method 1
from django.views.decorators.csrf import csrf_exempt #***Method 1

from rest_framework.decorators import api_view #***Method 2
from rest_framework.response import Response #***Method 2
from rest_framework import status

from .serializers import ArticleSerializers
from .models import Article

# Create your views here.
#***Method 2: Use api_views
@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializers(article, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#*** Method 2 : api_views
@api_view(["Get", "PUT", "DELETE"])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk = pk)
    except Article.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializers(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#***Method 1 : use csrf_exempt 
# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         article = Article.objects.all()
#         serializer = ArticleSerializers(article, many = True)
#         return JsonResponse(serializer.data, safe = False)
    
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializers(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)

#***Method 1 : Use csrf_exempt
# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk = pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status = 404)
    
#     if request.method == "GET":
#         serializer = ArticleSerializers(article)
#         return JsonResponse(serializer.data)
    
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializers(article, data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status = 400)
    
#     elif request.method == "DELET":
#         article.delete()
#         return HttpResponse(status = 204)