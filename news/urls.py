# news/urls.py
from django.urls import path
from .views import NewsListView, NewsDetailView
 
urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('<int:pk>', NewsDetailView.as_view(), name='news-detail'),
]