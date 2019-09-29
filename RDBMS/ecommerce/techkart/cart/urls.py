from django.urls import path
from . import views
app_name="cart"

urlpatterns = [
path('addtocart', views.addtocart, name="addtocart"),
path('opencart',views.opencart,name="opencart"),
path('checkout',views.checkout,name="checkout"),
path('checkoutdetails',views.checkoutdetails,name="checkoutdetails"),
path('handlerequest',views.handlerrequest,name="handlerequest")
]