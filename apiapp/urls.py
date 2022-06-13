from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.showPatterns, name='showpatterns'),
    path('view/', views.getData, name='getdata'),
    path('view/<str:name>/', views.getSpecificData, name='getspecificdata'),
    path('update/<str:name>/', views.updateData, name='updatedata'),
    path('add/', views.addData, name='adddata'),
    path('delete/<str:name>/', views.deleteData, name='deletedata'),
]
