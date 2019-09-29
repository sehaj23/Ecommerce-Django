import cgi

from django.contrib.auth.models import User
from django.shortcuts import render
from .models import addcart, pendingorder,customerbillingaddress
from django.shortcuts import HttpResponse
from django.contrib import messages,auth
from productlist.models import listing
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
MERCHANT_KEY = 'lxdacVt2@DhfE4BQ';
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

    products = addcart.objects.filter(cid_id=cid).filter(pid_id=pi).values()
    pro = listing.objects.filter(id=pi)



    context = {
        "pro": pro,
        "products": products
    }
    return render(request, "cart/checkout.html", context)

def checkout(request):
    pi = request.POST.get("listingid")
    cid = request.user.id

    products = addcart.objects.filter(cid_id=cid).filter(pid_id=pi).values()
    pro = listing.objects.filter(id=pi)



    context = {
        "pro" : pro,
        "products":products
    }
    d = pendingorder()
    orders = addcart.objects.filter(cid=cid)
    d.pid = listing.objects.get(pk=pi)
   # d.pid = orders.pid_id
    d.cid = request.user
    d.quantity = request.POST.get("quantity")

   # d.pid = listing.objects.filter(id=orders)
    d.save()
    return render(request,"cart/checkout.html",context)








def checkoutdetails(request):
    cid = request.user.id
    if request.method == "POST":

        c = customerbillingaddress()
        listingid = request.POST.get("listingid")
        c.cid = request.user
        c.fname = request.POST.get("fname")
        name = request.POST.get("fname")
        c.lname = request.POST.get("lname")
        c.address = request.POST.get("address")
        c.city = request.POST.get("city")
        c.state = request.POST.get("state")
        c.country = request.POST.get("country")
        c.zipcode = request.POST.get("zipcode")
        c.contact = request.POST.get("contact")
        c.quantity = request.POST.get("quantity")
        amount = request.POST.get("amount")
        c.amount = request.POST.get("amount")
        cartidd =  pendingorder.objects.filter(cid_id=cid).values("id")[:1]

        c.cartid = pendingorder.objects.get(id=cartidd)

        c.save()
        order_id = c.id
        print(order_id)
        messages.success(request,"address saved")
        param_dict = {
            'MID': 'yDZuTr04800090412050',
            'ORDER_ID': str(order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': str(cid),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerrequest',
        }
        param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,"cart/paytm.html",{'param_dict': param_dict})
       # return render(request,"productlist/index.html")

    else:
        messages.error(request, "error in address")
        return render(request,"cart/checkout.html")

@csrf_exempt
def handlerrequest(request): #paytm will handle   post request here
    form = cgi.FieldStorage()
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'cart/paymentstatus.html', {'response': response_dict})