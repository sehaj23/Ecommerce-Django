from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    return render(request,"accounts/userRegister.html")

def login(request):
    return render(request,"accounts/userLogin.html")

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,"accounts/dashboard.html")