

from django.shortcuts import render, get_object_or_404, HttpResponse, redirect,HttpResponseRedirect

from .models import listing, productreviews

from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    alllisting = listing.objects.all()
    storage = listing.objects.filter(category="storage")[:3]
    Smartphones = listing.objects.filter(category="Smartphones")[:3]
    laptop = listing.objects.filter(category="Laptops")[:3]
    headphones = listing.objects.filter(category="headphones")[:3]

    context = {"alllisting": alllisting,
               "storage": storage,
               "Smartphones": Smartphones,
               "laptop": laptop,
               "headphones": headphones
               }

    return render(request, "productlist/index.html", context)


def listingss(request, listing_id):
    category = listing.objects.filter(category="mobile")
    Listing = get_object_or_404(listing, pk=listing_id)




    reviews = productreviews.objects.filter(id=listing_id)

    #name = productreviews.objects.values(reviews)
   # Auth_user  = productreviews.cid

    userid  = productreviews.objects.filter(id=listing_id).values_list("cid",flat=True)
    querysetcount = userid.count()

    #iddd = User.objects.filter(id=userid)

    #print("idd is ",iddd)

  #  print("user id is ",userid.id)
   # user  = User.objects.get(id=userid.id)





    context = {"Listing": Listing,
               "category": category,
               "reviews":reviews,

                #"user":user
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


#def gotocart(request,listing_id):
 #   return render(request,"productlist/index.html")

"""
def post(request):
    preview = productrev()
    return render(request,"productlist/product.html",{'form':preview})

"""

def laptop(request):
    laptop = listing.objects.filter(category="Laptops")[:5]
    laptops = listing.objects.filter(category="Laptops")[5:10]
    context = {
            "laptop":laptop,
            "laptops": laptops

    }
    return render(request,"productlist/laptop.html",context)


