from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/register.html')

def leader_view_task(request):
    return render(request, 'leader/view_task.html')

def leader_view_user(request):
    return render(request, 'leader/view_user.html')
