from django.urls import path
# from .views import article_list, article_detail
# from .views import ArticleListAPIViews, ArticleDetailAPIView
from .views import ArticleGenericAPIView

urlpatterns = [
    # path('article/', views.article_list, name = 'article-list' ), #***use for method 1 and 2 (csrf-exemp and apai_view)
    # path('article/', ArticleListAPIViews.as_view()), #***Use for method 3 in (APIView Class)
    # path('detail/<int:pk>/', article_detail, name = 'article-detail' ), #***use for method 1 and 2 (csrf_exemp and api_view)
    # path('detail/<int:id>/', ArticleDetailAPIView.as_view() ), #***Use for method 3 (APIView Class)
    path('article/<int:id>/', ArticleGenericAPIView.as_view()), #***Use for method 4 (GenericAPIView)
    path('article/', ArticleGenericAPIView.as_view()) #***Use for method 4 (GenericAPIView)


]
