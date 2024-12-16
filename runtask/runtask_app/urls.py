from django.urls import path
from . import views
from .views import runtask

urlpatterns = [
    path('', views.runtask, name = 'runtask'),

    path('member/login/', views.member_login, name = 'member_login'),
    path('member/register/', views.member_register, name='member_register'),
    path('member/view-task/', views.member_view_task, name='member_view_task'),
    path('member/view-user/', views.member_view_user, name='member_view_user'),
    path('member/menu-label/', views.member_menu_label, name='member_menu_label'),
    path('member/settings/', views.member_settings, name='member_settings'),

    path('leader/login/', views.leader_login, name = 'leader_login'),
    path('leader/register/', views.leader_register, name = 'leader_register'),
    path('leader/view-task/', views.leader_view_task, name = 'leader_view_task'),
    path('leader/view-user/', views.leader_view_user, name='leader_view_user'),
    path('leader/menu-label/', views.leader_menu_label, name='leader_menu_label'),
    path('leader/settings/', views.leader_settings, name='leader_settings'),
]