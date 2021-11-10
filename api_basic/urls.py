from django.urls import path
from django.urls.conf import include
# from .views import article_list, article_detail
# from .views import ArticleListAPIViews, ArticleDetailAPIView
# from .views import ArticleGenericAPIView
# from .views import ArticleViewSet#***Use for method 5 (ViewSet)
from .views import ArticleGenericViewSet #*** Use for method 6 (GenericViewSet)
from rest_framework.routers import DefaultRouter#***Use for method 5&6 (ViewSet, GenericViewSet)


# router = DefaultRouter()#***Use for method 5 (ViewSet)
# router.register('article', ArticleViewSet, basename='article' )#***Use for method 5 (ViewSet)

router = DefaultRouter()#***Use for method 5 (ViewSet)
router.register('article', ArticleGenericViewSet, basename='article' )#***Use for method 5 (ViewSet)


urlpatterns = [
    # path('article/', views.article_list, name = 'article-list' ), #***use for method 1 and 2 (csrf-exemp and apai_view)
    # path('detail/<int:pk>/', article_detail, name = 'article-detail' ), #***use for method 1 and 2 (csrf_exemp and api_view)
    # path('apiview/detail/<int:id>/', ArticleDetailAPIView.as_view() ), #***Use for method 3 (APIView Class)
    # path('apiview/article/', ArticleListAPIViews.as_view()), #***Use for method 3 in (APIView Class)
    # path('generic/article/', ArticleGenericAPIView.as_view()) #***Use for method 4 (GenericAPIView)
    # path('generic/article/<int:id>/', ArticleGenericAPIView.as_view()), #***Use for method 4 (GenericAPIView)
    # path ('viewset/', include(router.urls)), #***Use for method 5 (ViewSet)
    # path ('viewset/<int:pk>', include(router.urls)), #***Use for method 5 (ViewSet)
    path('genericviewset/', include(router.urls)),#***Use for method 6 (GenericViewSet)
    path('genericviewset/<int:pk>', include(router.urls)),#***Use for method 5 (GenericViewSet)


]
