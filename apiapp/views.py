from importlib.metadata import packages_distributions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apiapp import serializers
from apiapp.models import Person
from apiapp.serializers import PersonSerializer
from django.contrib import messages
# Create your views here.


@api_view(['GET'])
def showPatterns(request):
    """ This function shows all the url patterns made available by this API """
    urlpatterns = {  
    '': 'urlpatterns',
    'View data': 'api-auth/view/',
    'Swagger UI': 'swagger/',
    'View specific data': 'api-auth/view/<str:name>',
    'Add data': 'api-auth/add/',
    'Update data': 'api-auth/update/<str:name>',
    'Delete data': 'api-auth/delete/<str:name>',
    }
    return Response(urlpatterns)

@api_view(['GET'])
def getData(request):
    """ This function is used to get the data from the database model """
    #person = {'name': 'Dhananjay', 'age':28}
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    
    return Response(serializer.data, 200)

@api_view(['GET'])
def getSpecificData(request, id):
    """ This function is used to get the data of specific Id item from the database """
    person = Person.objects.get(id=id)
    serializer = PersonSerializer(person)
    
    return Response(serializer.data)
    

@api_view(['POST'])
def addData(request):
    """ This function is used to add the data to the database """
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    data = serializer.data    
    return Response(data, 201)
    #alldata = Person.objects.all()
    #alldataserializer = PersonSerializer(alldata, many=True)
    #return Response(alldataserializer.data)
    
@api_view(['POST'])
def updateData(request, id):
    """ This function is used to update the data in the database """
    person = Person.objects.get(id=id)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request, id):
    """ This function is used to update the delete the data from the database """
    person = Person.objects.get(id=id)
    person.delete()
    return Response('Item Deleted')
