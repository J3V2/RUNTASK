from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def runtask(request):
    return render(request, 'login/runtask.html')

# Member
def member_login(request):
    return render(request, 'login/member_login.html')

def member_register(request):
    return render(request, 'login/member_register.html')

def member_view_task(request):
    return render(request, 'member/view_task.html')

def member_view_user(request):
    return render(request, 'member/view_user.html')

def member_menu_label(request):
    return render(request, 'member/menu_label.html')

def member_settings(request):
    return render(request, 'member/settings.html')


# Leader
def leader_login(request):
    return render(request, 'login/leader_login.html')

def leader_register(request):
    return render(request, 'login/leader_register.html')

def leader_view_task(request):
    return render(request, 'leader/view_task.html')

def leader_view_user(request):
    return render(request, 'leader/view_user.html')

def leader_menu_label(request):
    return render(request, 'leader/menu_label.html')

def leader_settings(request):
    return render(request, 'leader/settings.html')
