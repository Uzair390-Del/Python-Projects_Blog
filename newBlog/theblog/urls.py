from django.urls import path
from . import views
from django.conf import settings  # Add this import
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
     path('courses/', views.courses_list, name='courses_list'),  # List all courses
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),  # Detail view of a single course
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
     path('subscribe/', views.subscribe, name='subscribe'), 
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
