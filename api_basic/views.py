from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import authentication

# from django.http import HttpResponse, JsonResponse, response #***Mehtod 1
# from rest_framework import serializers #***Method 1
# from rest_framework.parsers import JSONParser #***Method 1
# from django.views.decorators.csrf import csrf_exempt #***Method 1

# from rest_framework.decorators import api_view #***Method 2
from rest_framework.response import Response #***Method 2 and Method 3
from rest_framework import status #***Method 2 and Method 3
from rest_framework.serializers import Serializer #***Method 2 and Method 3

from rest_framework.views import APIView #***Method 3

from rest_framework import generics#***Method 4
from rest_framework import mixins #***Method 4

from rest_framework.authentication import SessionAuthentication, BasicAuthentication #***For Authentication
from rest_framework.permissions import IsAuthenticated #***For Authentication

from .serializers import ArticleSerializers
from .models import Article

# Create your views here.

#***Method 4 : Use generic view and mixins 
class ArticleGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    lookup_field = 'id'

    authentication_classes = [SessionAuthentication, BasicAuthentication] #***For Authentication -> first session auth, second basic auth
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self, request, id = None):
        return self.destroy(request, id)


# #***Method 3: Use class method for api (APIView)
# class ArticleListAPIViews(APIView):
    
#     def get(self, request):
#         article = Article.objects.all()
#         serializer = ArticleSerializers(article, many = True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# #***Method 3: Use class method for api (APIView)
# class ArticleDetailAPIView(APIView):
#     def get_object(self, id):
#         try:
#             return Article.objects.get(id = id)
#         except Article.DoesNotExist:
#             return HttpResponse (status = status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#       article = self.get_object(id)
#       serializer = ArticleSerializers(article)
#       return Response(serializer.data)  
    
#     def put (self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializers(article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)


#***Method 2: Use api_views
# @api_view(["GET", "POST"])
# def article_list(request):
#     if request.method == "GET":
#         article = Article.objects.all()
#         serializer = ArticleSerializers(article, many = True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = ArticleSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#*** Method 2 : api_views
# @api_view(["Get", "PUT", "DELETE"])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk = pk)
#     except Article.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializers(article)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ArticleSerializers(article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

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