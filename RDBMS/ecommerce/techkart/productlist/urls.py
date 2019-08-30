from django.urls import path
from . import views
app_name="productlist"
urlpatterns = [
    path('',views.index,name="listings"),
    path('<int:listing_id>',views.listingss,name="listing"),
    path('search',views.search,name="search"),
    path('laptop',views.laptop,name="laptop"),
    path('camera', views.camera, name="camera"),
    path('smartphones',views.smartphones,name="smartphones"),
    path('accessories',views.accessories,name="accessories"),
    path('hotdeals',views.hotdealss,name="hotdeals"),
    path('hotdeals<int:hotdeals_id>',views.hotdealsinfo,name="hotdealsinfo"),



]
