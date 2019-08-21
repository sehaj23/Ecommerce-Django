import random
import string
from datetime import date, datetime

from django.shortcuts import render, get_object_or_404, HttpResponse, redirect,HttpResponseRedirect

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

    reviews = productreviews.objects.filter(id=listing_id)
    #name = productreviews.objects.values(reviews)
   # Auth_user  = productreviews.cid

    userid  = productreviews.objects.filter(id=listing_id).values_list("cid",flat=True)
    querysetcount = userid.count()

    user  = User.objects.get(id=userid[1])





    context = {"Listing": Listing,
               "category": category,
               "reviews":reviews,
                "user":user
               }
    return render(request, "productlist/product.html", context)


def search(request,listing_id):
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


def gotocart(request,listing_id):
    return render(request,"productlist/index.html")

"""
def addtocart(request,**kwargs):
    product = listing.objects.filter(id=kwargs.get("id","")).first()
    user = request.user
    savetocart = cart(cart_id=generate_order_id(),product)



    return render(request,"/product.html")

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str
"""
"""
def postreviews(request):
    if request.method == "post":
        post = productrev()
        post.rhead = request.POST["reviews"]
        post.rating = request.POST["rating"]
        post.data = request.POST["data"]
        post.save()
        return render(request, "/product.html")
    else:
        return render(request,"/product.html")


def post(request):
    preview = productrev()
    return render(request,"productlist/product.html",{'form':preview})

"""
