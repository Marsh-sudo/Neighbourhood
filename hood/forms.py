from dataclasses import field, fields
import email
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import Business,Profile,Neighbourhood

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

User._meta.get_field('email')._unique = True 
