from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import listing, productreviews

from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    alllisting = listing.objects.all()
    storage = listing.objects.filter(category="Storage")
    mobile = listing.objects.filter(category="mobile")
    laptop = listing.objects.filter(category="laptop")
    headphones = listing.objects.filter(category="headphones")

    context = {"alllisting": alllisting,
               "storage": storage,
               "mobile": mobile,
               "laptop": laptop,
               "headphones": headphones
               }
    return render(request, "productlist/index.html", context)


def listingss(request, listing_id):
    category = listing.objects.filter(category="mobile")
    Listing = get_object_or_404(listing, pk=listing_id)

    context = {"Listing": Listing,
               "category": category
               }
    return render(request, "productlist/product.html", context)


def search(request):
    queryset_list = listing.objects.all()

    if "keywords" in request.GET:
        keywords = request.GET['keywords']

        if keywords:
            queryset_list = queryset_list.filter(p_name__icontains=keywords)

    context = {
        'queryset_list': queryset_list,
        'values': request.GET
    }

    return render(request, "productlist/search.html", context)


def postreviews(request):
    if request.method == "post":
        post = productreviews()
        post.rhead = request.POST.get["reviews"]
        post.rating = request.POST.get["rating"]
        post.save()
        return render(request, "/product.html")
    else:
        return render(request,"/index.html")
