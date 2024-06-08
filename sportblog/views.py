from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>My sport blog</h1>")

def about(request):
    return HttpResponse("Blog About")