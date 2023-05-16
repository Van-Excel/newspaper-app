from django.urls import path
from .views import ArticlesListView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView, ArticleCreateView


urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticlesListView.as_view(), name='article_list'),
]
