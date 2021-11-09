from django.db.models import fields
from rest_framework import serializers
from .models import Article


#*** Method 1 :
# class ArticleSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

#*** Method 2 :
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author', 'email'] #* Method 1
        fields = '__all__' #*Method 2