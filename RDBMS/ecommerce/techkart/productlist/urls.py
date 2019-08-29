from django.urls import path
from . import views
app_name="productlist"
urlpatterns = [
    path('',views.index,name="listings"),
    path('<int:listing_id>',views.listingss,name="listing"),
    path('search',views.search,name="search"),
    path('laptop',views.laptop,name="laptop"),


]
