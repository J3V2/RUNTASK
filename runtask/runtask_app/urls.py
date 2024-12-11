from django.urls import path
from . import views
from .views import login

urlpatterns = [
    path('', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('leader/view-task', views.leader_view_task, name = 'leader_view_task'),
    path('leader/view-user', views.leader_view_user, name='leader_view_user')
]