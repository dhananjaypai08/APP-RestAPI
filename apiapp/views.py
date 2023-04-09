from rest_framework.response import Response
from rest_framework.decorators import api_view
from apiapp import serializers
from apiapp.models import Dog, User, Like
from apiapp.serializers import DogSerializer, UserSerializer, LikeSerializer



@api_view(['GET'])
def showPatterns(request):
    """ This function shows all the url patterns made available by this API """
    urlpatterns = {  
    '': 'urlpatterns',
    'Register': 'api-auth/register/',
    'View data': 'api-auth/view/',
    'Swagger UI': 'swagger/',
    'View specific data': 'api-auth/view/<str:name>',
    'Add data': 'api-auth/add/',
    'Update data': 'api-auth/update/<str:name>',
    'Delete data': 'api-auth/delete/<str:name>',
    }
    return Response(urlpatterns)

@api_view(['POST'])
def register(request):
    """ This function is used to save the new users data in database """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('saved')
        data = serializer.data    
        return Response(data)
    return Response("Item not Added")

@api_view(['GET'])
def getData(request):
    """ This function is used to get the data from the database model """
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    
    return Response(serializer.data, 200)

@api_view(['GET'])
def getSpecificData(request, id):
    """ This function is used to get the data of specific Id item from the database """
    person = Dog.objects.get(id=id)
    serializer = DogSerializer(person)
    
    return Response(serializer.data)
    

@api_view(['POST'])
def addData(request):
    """ This function is used to add the data to the database """
    serializer = DogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('saved')
        data = serializer.data    
        return Response(data)
    return Response("Item Not Added")
    
@api_view(['POST'])
def updateData(request, id):
    """ This function is used to update the data in the database """
    person = Dog.objects.get(id=id)
    serializer = DogSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('saved in database')
    
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request, id):
    """ This function is used to delete the data from the database """
    person = Dog.objects.get(id=id)
    person.delete()
    return Response('Item Deleted')

@api_view(['GET'])
def addlikes(request, dog_id):
    """ This function is used to store likes of Dogs """
    user_id = request.session.get("user_id")
    if user_id:
        user = User.objects.get(id=user_id)
        dog = Dog.objects.get(id=dog_id)
        likes = Like.objects.filter(user=user, dog=dog)
        if len(likes)>0:
            pass 
        else:
            dog.likes += 1
            dog.save()
            likes = Like(user=user, dog=dog)
            likes.save()
        return Response(dog.likes)
    else:
        return Response("Something went wrong")
            
        
        
