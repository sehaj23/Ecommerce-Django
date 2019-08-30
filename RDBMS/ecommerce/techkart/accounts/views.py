from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        username= request.POST["username"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        #check if password match
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email ID already registered")
                return redirect('productlist:register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                #login after register
                auth.login(request,user)
                messages.success(request,"You are now Logged in")
                return redirect('productlist:listings')
        else:
            messages.error(request,"password does not match")
            return redirect('accounts:register')

    else:
        return render(request,"accounts/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect("productlist:listings")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("accounts:login")
    else:
        return render(request,"accounts/login.html")

def logout(request):
    auth.logout(request)
    return redirect("productlist:listings")