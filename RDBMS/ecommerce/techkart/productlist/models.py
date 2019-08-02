from django.db import models

# Create your models here.
class listing(models.Model):
    id = models.IntegerField(max_length=10,primary_key=True)
    p_name = models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    quantity=models.IntegerField(max_length=10)
    price = models.IntegerField(max_length=100)
    description = models.TextField(max_length=200)
    p_color = models.CharField(max_length=100)
    mainphoto = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo1 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    def __str__(self):
        return self.p_name

class users(models.Model):
    u_id =models.IntegerField(max_length=50)
    u_fname=models.CharField(max_length=200)
    u_lname=models.CharField(max_length=200)
    u_email=models.EmailField(max_length=200)
    u_gender=models.CharField(max_length=200)
    u_mobile=models.IntegerField(max_length=13)
    u_city=models.CharField(max_length=100)
    u_address=models.CharField(max_length=100)
    u_state=models.CharField(max_length=100)
    u_zipcode=models.IntegerField(max_length=200)
    def __str__(self):
        return self.u_fname
