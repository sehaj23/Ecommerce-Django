from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        return HttpResponse("submited")
    else:
        return render(request,"accounts/userRegistration.html")

def login(request):
    return render(request,"accounts/userLogin.html")

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,"accounts/dashboard.html")