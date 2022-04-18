from dataclasses import field, fields
import email
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import Business,Profile,Neighbourhood,Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

User._meta.get_field('email')._unique = True 


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name','description','business_photo','email']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_pic','bio','neighbourhood']

        widgets = {
            'bio':Textarea(attrs={'cols':30,'rows':5}),
        }

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','post','author']