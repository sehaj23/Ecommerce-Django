from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="listings"),
    path('<int:listing_id>',views.listingss,name="listing"),
    path('search',views.search,name="search"),
   path('cart<int:listing_id>', views.gotocart, name="gotocart"),

]
