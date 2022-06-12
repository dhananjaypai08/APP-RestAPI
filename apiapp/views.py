from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apiapp.models import Person
from apiapp.serializers import PersonSerializer
from django.contrib import messages
# Create your views here.

@api_view(['GET'])
def getData(request):
    #person = {'name': 'Dhananjay', 'age':28}
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    data = serializer.data
    messages.add_message(request, messages.SUCCESS, 'Person created!')
    return Response(data)
    #alldata = Person.objects.all()
    #alldataserializer = PersonSerializer(alldata, many=True)
    #return Response(alldataserializer.data)

'''
@api_view(['DELETE'])
def deleteData(request):
    person = Person.objects.get(name=request.data)
    serializer = PersonSerializer(data=person)
    person.delete()
    return Response(serializer.data)
'''