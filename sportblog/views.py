from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic
from .models import Homepage


# Create your views here.
def home(request):
    home_data = Homepage.objects.all()

    if not home_data:
        return render(request, 'sportblog/home.html', {'error': 'No homepage data found.'})

    try:
        first_item = home_data[0]
    except IndexError:
        first_item = None  # Handle the case where the list is empty

    context = {
        'first_item': first_item,
    }
    return render(request, 'sportblog/home.html', context)
    
def about(request):
    return render(request, 'sportblog/about.html')

def contact(request):
    return render(request, 'sportblog/contat.html')

def post_details(request):
    return render(request, 'sportblog/post_details.html')
