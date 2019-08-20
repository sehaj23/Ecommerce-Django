from django.contrib import admin

# Register your models here.

from .models import listing



class listingadmmin(admin.ModelAdmin):
    list_display = ('id','p_name','price',"quantity","category")
    list_display_links = ('id','p_name')
    list_filter = ("price","category","quantity")
    search_fields = ("p_name","category","price")

admin.site.register(listing,listingadmmin)

#class reviewadmin(admin.ModelAdmin):
    #list_display = ('id','cid','pid','rhead')

#admin.site.register(reviewss)
