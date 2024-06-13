from django.urls import path
from .  import views


urlpatterns = [
    path('', views.home, name='sportblog-home'),
    path('about/', views.about, name='sportblog-about'),
    path('post/', views.post_details, name='sportblog-post'),
    path('contact/', views.contact, name='blog-contact'),
]