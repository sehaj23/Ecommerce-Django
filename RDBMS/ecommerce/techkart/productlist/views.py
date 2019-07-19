from django.shortcuts import render
from .models import listing
# Create your views here.

def index(request):
    alllisting = listing.objects.all()
    context = { "alllisting": alllisting}
    return render(request,"productlist/listing.html",context)

def listingss(request):
    return render(request,"productlist/product.html")
