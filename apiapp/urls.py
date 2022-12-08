from django.urls import path
from apiapp import views
from rest_framework import permissions
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="API Build")
'''
schema_view = get_schema_view(
   openapi.Info(
      title="API Building",
      default_version='v1',
      description="Testing locally built API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dhananjay2002pai@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
'''

urlpatterns = [
    path('', views.showPatterns, name='showpatterns'),
    path('register/', views.register, name='register'),
    path('swagger/', schema_view),
    #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('view/', views.getData, name='getdata'),
    path('view/<int:id>/', views.getSpecificData, name='getspecificdata'),
    path('update/<int:id>/', views.updateData, name='updatedata'),
    path('add/', views.addData, name='adddata'),
    path('delete/<int:id>/', views.deleteData, name='deletedata'),
]
