from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list, name = 'article-list' ),
    path('detail/<int:pk>/', views.article_detail, name = 'article-detail' ),
]
