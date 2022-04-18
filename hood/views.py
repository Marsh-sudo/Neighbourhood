from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Profile,Business
from .forms import BusinessForm,UpdateUserForm,UpdateUserProfileForm

# Create your views here.
# @login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'all-neighbor/home.html')

def hoods(request):
    current_user = request.user
    hoods = Neighbourhood.objects.all()
    return render(request,'all-neighbor/estate.html',{'hoods':hoods,'current_user':current_user})


def estates(request,id):
    post = Neighbourhood.objects.get(id=id)
    # post = get_object_or_404(Neighbourhood,pk=id)
    # houses = Neighbourhood.objects.filter(hoods=id)

    return render(request,'all-neighbor/details.html',{"post":post})

def new_business(request,id):
    current_user = request.user
    if request.method == "POST":
        bus_form = BusinessForm(request.POST,request.FILES)
        bus_form.instance.user = request.user
        if bus_form.is_valid():
            bus_form.save()
            return redirect('my_estate',id)


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

    return render (request,'all-neighbor/profile.html',{"profile_form":profile_form,"profiles":profile})