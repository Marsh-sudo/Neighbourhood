from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Profile,Business


# Create your views here.
# @login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'all-neighbor/home.html')

def hoods(request):
    current_user = request.user
    hoods = Neighbourhood.objects.all()
    return render(request,'all-neighbor/estate.html',{'hoods':hoods,'current_user':current_user})


def estates(request,id):
    post = get_object_or_404(Neighbourhood,pk=id)
    # houses = Neighbourhood.objects.filter(hoods=id)

    return render(request,'all-neighbor/hoods.html',{"houses":post})