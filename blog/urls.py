from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),
    path('articles', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('poems', views.poem_list, name='poem_list'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('poem/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('miscellaneouss', views.miscellaneous_list, name='miscellaneous_list'),
    path('miscellaneous/<int:pk>/', views.miscellaneous_detail, name='miscellaneous_detail'),
    path('article/new/', views.article_new, name='article_new'), 
    path('poem/new/', views.poem_new, name='poem_new'),   
]