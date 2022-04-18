from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Post,Profile,Business
from .forms import BusinessForm,UpdateUserForm,UpdateUserProfileForm,NewPostForm

# Create your views here.
# @login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'all-neighbor/home.html')

def hoods(request):
    current_user = request.user
    hoods = Neighbourhood.objects.all()
    return render(request,'all-neighbor/estate.html',{'hoods':hoods,'current_user':current_user})


def estates(request,id):
    houses = Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(neighbourhood=id)
    businesses = Business.objects.filter(pk=id)
   

    return render(request,'all-neighbor/details.html',{"houses":houses,"posts":posts,"businesses":businesses})

def new_business(request,id):
    current_user = request.user
    if request.method == "POST":
        bus_form = BusinessForm(request.POST,request.FILES)
        bus_form.instance.user = request.user
        if bus_form.is_valid():
            bus_form.save()
            return redirect('my_estate',id)
    else:
        bus_form = BusinessForm()
    return render (request,'all-neighbor/business.html',{"bus_form":bus_form})


def profile(request):
    profile = Profile.display_profile()
    current_user = request.user

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        profile_form = UpdateUserProfileForm()

    return render (request,'all-neighbor/profile.html',{"profiles":profile})


def new_post(request,id):
    current_user = request.user
    if request.method == 'POST':
        post_form = NewPostForm(request.POST)
        post_form.instance.user = request.user
        if post_form.is_valid():
            post_form.save()
            return redirect('my_estate',id)
    else:
        post_form = NewPostForm()
    
    return render (request,'all-neighbor/post.html',{"post_form":post_form})

def leave_hood(request):
    # hood = Neighbourhood.objects.get(id=id)
    # request.user.profile.neighbourhood = None
    # request.user.profile.save()
    return redirect(request,'all-neighbor/estate.html')


def search_hood(request):
    if request.method == 'GET':
        name = request.GET.get("name")
        searched = Neighbourhood.objects.filter(name=name).all()

    return render (request,'all-neighbor/search.html',{"hoods":searched})

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profiles')
    else:
        profile_form = UpdateUserProfileForm()
    
    return render (request,'all-neighbor/new_profile.html',{"profile_form":profile_form})