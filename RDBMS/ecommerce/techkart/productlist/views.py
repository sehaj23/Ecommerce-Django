from django.shortcuts import render,get_object_or_404,HttpResponse
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

def search(request):
    queryset_list =listing.objects.all()

    if "keywords" in request.GET:
        keywords = request.GET['keywords']

        if keywords:
            queryset_list= queryset_list.filter(p_name__icontains=keywords)

    context={
                'queryset_list':queryset_list,
                'values':request.GET
            }

    return render(request, "productlist/search.html",context)
