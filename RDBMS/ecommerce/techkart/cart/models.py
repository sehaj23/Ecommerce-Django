from django.db import models
from productlist.models import listing
from django.contrib.auth import get_user_model
# Create your models here.

class addcart(models.Model):
    pid = models.ForeignKey(listing,on_delete=models.CASCADE)
    cid = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=20)

class customerbillingaddress(models.Model):
    cid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname  = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.IntegerField(max_length=10)
    contact=models.IntegerField(max_length=15)
    notes = models.CharField(max_length=100,blank=True)

class pendingorder(models.Model):
    pid = models.ForeignKey(listing,on_delete=models.CASCADE)
    cid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=20)
