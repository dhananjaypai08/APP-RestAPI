from django.shortcuts import render
import requests
import json
from apiapp.models import Person
# Create your views here.

def home(request):
    return render(request, 'index.html')

def listUser(request):
    msg = {}
    msg['search'] = 0
    msg['signal'] = 0
    if request.method=='POST':
        """ We can also use the api to fetch this information. Here we have fetched from our databse."""
        search = request.POST.get('search')
        if search.isdigit():
            id = int(search)
            data = Person.objects.get(id=id)
            usrdata = {
                "id": data.id,
                "name": data.name,
                "age": data.age,
                "created": data.created
            }
            msg['search'] = 1
        else:
            name = search
            data = Person.objects.filter(name=name)
            usrdata = {}
            
            for ind,usr in enumerate(data):
                lvl = {}
                lvl['id'] = usr.id
                lvl['name'] = usr.name
                lvl['age'] = usr.age
                lvl['created'] = usr.created
                usrdata[ind+1] = lvl
            msg['search'] = 2
        msg['filtereddata'] = usrdata
    try:
        data = getUsersData()
        msg['data'] = data
        msg['signal'] = 1
    except:
        msg['signal'] = 2
    print(msg)
    return render(request, 'userlist.html', msg)
        
def listSpecificUser(request):
    return render(request, 'listSpecificUser.html')

def addUser(request):
    msg = {}
    msg['added'] = 0
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        url = 'http://127.0.0.1:8000/api-auth/add/'
        try:
            age = int(age)
            data = requests.post(url, data={"name": name, "age": age})
            print(data) # Response code
            data = data.json()
            print(data)
            msg['added'] = 1
        except:
            msg['added'] = 2
        
    return render(request, 'add.html', msg)

def updateUser(request):
    return render(request, 'update.html')

def deleteUser(request):
    return render(request, 'delete.html')


def getUsersData():
    """ User data generation """
    url = 'http://127.0.0.1:8000/api-auth/view/'
    data = requests.get(url)
    data = data.json()
    
    return data