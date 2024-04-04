from . import views
from django.urls import path, include
from .views import course_detail





urlpatterns = [
    path('create-course/', views.create_course, name='create_course'),
    path('create-chapter/<int:course_id>/', views.create_chapter, name='create_chapter'),
    path('course/<slug:course_title>/', views.course_detail, name='course_detail'),
    path('chapters/<slug:filename>/', views.chapter_file_view, name='chapter_file'),




    

]