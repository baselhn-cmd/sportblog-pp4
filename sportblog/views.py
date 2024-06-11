from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contat.html')

def post_details(request):
    return render(request, 'blog/post_details.html')
