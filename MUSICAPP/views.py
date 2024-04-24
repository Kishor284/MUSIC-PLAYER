from django.shortcuts import render,redirect
from .models import signup
from .forms import Signupform
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.POST:
        frm = Signupform(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm=Signupform()
    return render(request, 'signup.html')