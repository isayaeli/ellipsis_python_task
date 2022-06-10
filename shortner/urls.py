from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('manage',views.manage, name='manage'),
    path('profile',views.profile, name='profile'),
    path('shorten', views.createurl, name='create'),
    path('success', views.success, name='success'),
     path('edit/<str:slug>', views.update_url, name='edit'),
    path('disable/<str:slug>', views.disable_url,name='disable'),
    path('delete/<str:slug>', views.delete_url, name='delete'),
    # path('<str:slug>', views.exit, name='exit'),
    
]