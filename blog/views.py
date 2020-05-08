from django.shortcuts import render
from .models import Blog

def home(request):
    comments = Blog.objects
    return render(request, 'home.html', {'comments' : comments})