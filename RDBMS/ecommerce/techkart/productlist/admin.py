from django.contrib import admin

# Register your models here.

from .models import listing,productreviews,hotdeals



class listingadmmin(admin.ModelAdmin):
    list_display = ('id','p_name','price',"quantity","category")
    list_display_links = ('id','p_name')
    list_filter = ("price","category","quantity")
    search_fields = ("p_name","category","price")

admin.site.register(listing,listingadmmin)

class reviewadmin(admin.ModelAdmin):
    list_display = ('rid','cid','id','rhead','rhead','star')

admin.site.register(productreviews,reviewadmin)


class deals(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'price', "quantity", "category", 'oldprice')
    list_display_links = ('id', 'p_name')
    list_filter = ("price", "category", "quantity")
    search_fields = ("p_name", "category", "price")

admin.site.register(hotdeals,deals)