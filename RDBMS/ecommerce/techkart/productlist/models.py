from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



class listing(models.Model):
    id = models.IntegerField(max_length=10,primary_key=True)
    p_name = models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    quantity=models.IntegerField(max_length=10)
    price = models.IntegerField(max_length=100)
    description = models.TextField(max_length=200)
    p_specification = models.TextField(max_length=600)
    p_color = models.CharField(max_length=100)
    mainphoto = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo1 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    def __str__(self):
       return self.p_name

class productreviews(models.Model):
    rid = models.IntegerField(max_length=20,primary_key=True)
    id = models.ForeignKey('listing', on_delete=models.CASCADE)
    cid = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    rhead= models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    star = models.IntegerField(max_length=1)
    class meta:
        db_table = "Productreviews"


