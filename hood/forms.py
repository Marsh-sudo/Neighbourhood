from dataclasses import field, fields
import email
from pyexpat import model
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
        fields ='__all__'
        

class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','location','description','logo','health_number','police_number']
        exclude = ['admin']

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
        fields ='__all__'