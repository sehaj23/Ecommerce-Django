from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello")

def about(request):
    return render(request,"pages/index.html")

def register(request):
    return render(request,"pages/product.html")