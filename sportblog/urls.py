from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="sportblog-home"),
    path('about', views.about, name="blog-about"),
    path('contact', views.contact, name="blog-contat"),
    path('post', views.about, name="blog-post"),
]