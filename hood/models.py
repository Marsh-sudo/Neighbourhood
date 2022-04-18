
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=300,blank=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    logo =  models.ImageField(upload_to='images/')
    health_number = models.IntegerField(blank=True,default=0)
    police_number = models.IntegerField(blank=True,default=0)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name} hood'

    @classmethod
    def display(cls):
        posts = cls.objects.all()
        return posts


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=200,blank=True)
    name = models.CharField(max_length=250,blank=True)
    profile_pic = models.ImageField(upload_to='images/')
    neighbourhood = models.ForeignKey(Neighbourhood,null=True,blank=True,on_delete=models.CASCADE)

    @classmethod
    def display_profile(cls):
        profile = cls.objects.all()
        return profile



class Business(models.Model):
    business_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_photo = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)