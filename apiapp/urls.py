from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.showPatterns, name='showpatterns'),
    path('view/', views.getData, name='getdata'),
    path('view/<int:id>/', views.getSpecificData, name='getspecificdata'),
    path('update/<int:id>/', views.updateData, name='updatedata'),
    path('add/', views.addData, name='adddata'),
    path('delete/<int:id>/', views.deleteData, name='deletedata'),
]
