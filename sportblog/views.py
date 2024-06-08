from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'author': 'Destiny Franks',
        'title': 'Blog Post1',
        'content': 'This is my first blog post',
        'date_posted': '7th August, 2021',
    },

{
        'author': 'Jane Doe',
        'title': 'Blog Post2',
        'content': 'This is my second blog post',
        'date_posted': '7th August, 2021',
    }
    
]
# Create your views here.
def home(request):
    contex = {
        'posts': posts
    }
    return render(request, 'sportblog/home.html', context)

def about(request):
    return render(request, 'sprtblog/about.html')