from django.urls import path, include
from .views import Index
from .views import Index, DetailArticleView, LikeArticle, Featured, DeleteArticleView
from .views import CreateArticleView


urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('create/', CreateArticleView.as_view(), name='create_article'),
]
