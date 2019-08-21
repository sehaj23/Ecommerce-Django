from django.urls import path
from django.conf.urls import url
from . import views

app_name = "shoppingcart"
urlpatterns = [
path("<int:listing_id>",views.addtocart,name="addtocart")
]