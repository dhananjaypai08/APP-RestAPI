from django.urls import path 
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewuser/all/', views.listUser, name='listuser'),
    path('viewuser/', views.listSpecificUser, name='listspecificuser'),
    path('adduser', views.addUser, name='adduser'),
    path('updateuser/', views.updateUser, name='updateuser'),
    path('deleteuser/', views.deleteUser, name='deleteuser'),
]
