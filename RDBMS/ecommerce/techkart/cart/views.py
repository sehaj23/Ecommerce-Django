from django.contrib.auth.models import User
from django.shortcuts import render
from .models import addcart,customerbillingaddress,pendingorder
from django.shortcuts import HttpResponse
from django.contrib import messages,auth
from productlist.models import listing
# Create your views here.
def addtocart(request):
    if request.method == "POST":
        p = addcart()
        p.quantity = request.POST.get("quantity")
        pi = request.POST.get("listingid")
        p.cid = request.user
        p.pid = listing.objects.get(pk=pi) #creating instance
        p.save()
        cart = addcart.objects.filter(cid=p.cid)
        product = listing.objects.filter(id=pi)
        products = []
        products.append(product)
        context = {
            "quantity":p.quantity,

            "cart":cart,
            "product":product
        }




        return render(request,"cart/viewCart.html",context)

def opencart(request):
    pi = request.POST.get("listingid")
    cid = request.user.id
    print(pi)
    products = addcart.objects.filter(cid_id=cid).filter(pid_id=pi).values()
    pro = listing.objects.filter(id=pi)
    print(pro)

    print(products)
    context = {
        "pro": pro,
        "products": products
    }
    return render(request, "cart/checkout.html", context)

def checkout(request):
    pi = request.POST.get("listingid")
    cid = request.user.id
    print(pi)
    products = addcart.objects.filter(cid_id=cid).filter(pid_id=pi).values()
    pro = listing.objects.filter(id=pi)
    print(pro)

    print(products)
    context = {
        "pro" : pro,
        "products":products
    }
    return render(request,"cart/checkout.html",context)
"""
cid = request.user.id
d = pendingorder()

orders = addcart.objects.filter(cid=cid)
d.pid = orders.pid
d.cid = request.user
# d.pid = listing.objects.filter(id=orders)
d.save()
"""



def checkoutdetails(request):
    if request.method == "POST":
        c = customerbillingaddress()
        c.cid = request.user
        c.fname = request.POST.get("fname")
        c.lname = request.POST.get("lname")
        c.address = request.POST.get("address")
        c.city = request.POST.get("city")
        c.state = request.POST.get("state")
        c.country = request.POST.get("country")
        c.zipcode = request.POST.get("zipcode")
        c.contact = request.POST.get("contact")
        c.save()
        messages.success(request,"address saved")
        return render(request,"productlist/index.html")

    else:
        messages.error(request, "error in address")
        return render(request,"cart/checkout.html")


