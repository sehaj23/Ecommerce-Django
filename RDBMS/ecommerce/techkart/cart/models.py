from django.db import models
from productlist.models import listing
from django.contrib.auth import get_user_model
# Create your models here.

class addcart(models.Model):
    pid = models.ForeignKey(listing,on_delete=models.CASCADE)
    cid = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=20)



class pendingorder(models.Model):
    pid = models.ForeignKey(listing,on_delete=models.CASCADE)
    cid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=20)


class customerbillingaddress(models.Model):
    cid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cartid = models.ForeignKey(pendingorder, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname  = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    notes = models.CharField(max_length=100,default="NULL",blank=True)
    quantity = models.IntegerField(max_length=100)
    amount = models.IntegerField(max_length=100,default=0)
