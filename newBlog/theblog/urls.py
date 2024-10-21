from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
     path('subscribe/', views.subscribe, name='subscribe'), 
]
