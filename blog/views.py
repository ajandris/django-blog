from django.shortcuts import render, HttpResponse

# Create your views here.

def my_blog(request):
    return HttpResponse("Hello, Blog!")
