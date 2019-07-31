from django.shortcuts import render,get_object_or_404
from .models import listing
# Create your views here.

def index(request):
    alllisting = listing.objects.all()
    context = { "alllisting": alllisting}
    return render(request,"productlist/index.html",context)

def listingss(request,listing_id):
    Listing = get_object_or_404(listing,pk=listing_id)
    context = {"Listing": Listing}
    return render(request,"productlist/product.html",context)
