from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Neighbourhood, Post,Profile,Business
from .forms import BusinessForm,UpdateUserForm,UpdateUserProfileForm,NewPostForm,NewHoodForm

# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'all-neighbor/home.html')

def new_hood(request):
    current_user = request.user
    if request.method == "POST":
        form = NewHoodForm(request.POST,request.FILES)
        form.instance.admin = request.user
        print(form)
        if form.is_valid():
            
            form.save()

            return redirect('estates')
    else:
        form = NewHoodForm()

    return render(request,'all-neighbor/newhood.html',{"form":form})


def hoods(request):
    current_user = request.user
    hoods = Neighbourhood.objects.all()
    return render(request,'all-neighbor/estate.html',{'hoods':hoods,'current_user':current_user})


def estates(request,id):
    posts = Post.objects.all()
    houses = Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(neighbourhood=houses)
    businesses = Business.objects.filter(location=houses)
   

    return render(request,'all-neighbor/details.html',{"houses":houses,"posts":posts,"businesses":businesses})

def new_business(request,id):
    current_user = request.user
    if request.method == "POST":
        bus_form = BusinessForm(request.POST,request.FILES)
        if bus_form.is_valid():
            bus_form.instance.user = request.user
            bus_form.location = Neighbourhood.objects.filter(id=id)
            bus_form.save()
            # return redirect('my_estate',id)
            next=request.GET.get('next', reverse('estates'))
            return  HttpResponseRedirect(f'/my_estate/{id}')
    else:
        bus_form = BusinessForm()
    return render (request,'all-neighbor/business.html',{"bus_form":bus_form})


def profile(request):
    profile = Profile.display_profile()


    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST,request.FILES)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
        
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    return render (request,'all-neighbor/profile.html',{"profiles":profile,"user_form":user_form,"profile_form":profile_form})


def new_post(request,id):
    current_user = request.user
    if request.method == 'POST':
        post_form = NewPostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.user = request.user
            post_form.author = Neighbourhood.objects.filter(id=id)
            post_form.save()
            # return redirect('my_estate',id)
            next=request.GET.get('next', reverse('estates'))
            return  HttpResponseRedirect(f'/my_estate/{id}')
    else:
        post_form = NewPostForm()
    
    return render (request,'all-neighbor/post.html',{"post_form":post_form})

def leave_hood(request,id):
    neighbourhood = get_object_or_404(Neighbourhood,pk=id)
    request.user.profile.neighbourhood = None
    return redirect(request,'all-neighbor/estate.html')


def search_hood(request):
    if request.method == 'GET':
        name = request.GET.get("name")
        searched = Neighbourhood.objects.filter(name=name).all()

    return render (request,'all-neighbor/search.html',{"hoods":searched})

# def new_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST,instance=request.user)
#         profile_form = UpdateUserProfileForm(request.POST,request.FILES)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('profiles')
#     else:
#         profile_form = UpdateUserProfileForm()
    
#     return render (request,'all-neighbor/new_profile.html',{"profile_form":profile_form})