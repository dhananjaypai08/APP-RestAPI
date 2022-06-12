from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.getData, name='getdata'),
    path('add', views.addData, name='adddata'),
    path('delete', views.deleteData, name='deletedata'),
]
