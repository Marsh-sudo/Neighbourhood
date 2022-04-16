
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    logo =  models.ImageField(upload_to='images/')


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=250,blank=True)
    name = models.CharField(max_length=250,blank=True)
    profile_pic = models.ImageField(upload_to='images/')
    neighbourhood = models.ForeignKey(Neighbourhood,null=True,blank=True,on_delete=models.CASCADE)


class Business(models.Model):
    business_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_photo = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)