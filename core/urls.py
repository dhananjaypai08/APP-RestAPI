from django.urls import path 
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='start'),
    path('register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('viewuser/all/', views.listUser, name='listuser'),
    path('viewuser/', views.listSpecificUser, name='listspecificuser'),
    path('adduser/', views.addUser, name='adduser'),
    path('updateuser/', views.updateUser, name='updateuser'),
    path('updateuser/updatinguser/', views.updatingUser, name='updatinguser'),
    path('deleteuser/', views.deleteUser, name='deleteuser'),
]
