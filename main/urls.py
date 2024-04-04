#-*- coding: utf-8 -*-

from django.urls import path, include
from . import views
from .views import home, courses ,index,contact   
from django.conf.urls.static import static
from django.conf import settings
from .views import CustomSignupView, CustomLoginView, custom_logout
from django.contrib import admin
from django.contrib.auth.decorators import login_required





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),

    path('courses_Page/', views.courses, name='courses'),
    path('courses.html', views.courses_html, name='courses_html'),
    path('index.html', views.index, name='index'),
    path('courses/', include('courses.urls')),
    path('accounts/signup/', CustomSignupView.as_view(), name='custom_signup'),  
    path('accounts/login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', custom_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('reset/', views.reset_view, name='password_reset'),

    path('accounts/', include('allauth.urls')),
    path('contact.html', views.contact, name='contact'),
   



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

