from django.shortcuts import render
import requests
import json
from apiapp.models import Dog
# Create your views here.

BASE_DIR = 'api/media/api/static'

def home(request):
    """ This is the root function for the core app """
    return render(request, 'index.html')

def listUser(request):
    """ This function is used for viewing and searching the data elements """
    msg = {}
    msg['search'] = 0
    msg['signal'] = 0
    if request.method=='POST':
        """ We can also use the api to fetch this information. Here we have fetched from our databse."""
        search = request.POST.get('search')
        idflg, ageflg, createdflg = request.POST.get('id'), request.POST.get('age'), request.POST.get('created')
        print(idflg, ageflg, createdflg)
        if search.isdigit():
            id = int(search)
            data = Dog.objects.get(id=id)
            usrdata = {
                "id": data.id,
                "name": data.name,
                "age": data.age,
                "created": data.created
            }
            msg['search'] = 1
        else:
            name = search
            data = Dog.objects.filter(name=name)
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
    return render(request, 'userlist.html', msg)
        
def listSpecificUser(request):
    return render(request, 'listSpecificUser.html')

def addUser(request):
    """ This function adds the new data to the database using the local API """
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
    """ This function provides the connectivity to `updatingUser` function """
    msg = {}
    msg['search'] = -1
    if request.method=='POST':
        search = request.POST.get('search')
        
        if search:
            if search.isdigit():
                usrid = int(search)
                data = Dog.objects.get(id=usrid)
                usrdata = {
                    "id": data.id,
                    "name": data.name,
                    "age": data.age,
                    "created": data.created
                }
                msg['search'] = 1
                
            else:
                data = Dog.objects.filter(name=search)
                usrdata = {}
                for ind, usr in enumerate(data):
                    lvl = {}
                    lvl['id'] = usr.id
                    lvl['name'] = usr.name
                    lvl['age'] = usr.age
                    lvl['created'] = usr.created
                    usrdata[ind+1] = lvl 
            msg['filtereddata'] = usrdata 
    url = 'http://127.0.0.1:8000/api-auth/view/'
    try:
        data = getUsersData()
        msg['data'] = data
        msg['signal'] = 1
        '''
        data = response.text
        jsondata = json.loads(data)
        actualdata = jsondata[0]
        '''
        
    except:
        msg['signal'] = 2
        print('\nError')
    
    return render(request, 'update.html',msg)


def store_id(gid):
    """ This function is to store the id of the updating element """
    global store
    store['id'] = gid
store = {}

def updatingUser(request):
    """ This function actually takes the data to be updated and updates the data """
    msg = {}
    msg['signal'] = -1
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        id = request.POST.get('id')
        print(id,name,age)
        if id is not None:
            store_id(id)
        if id:
            try:
                data = Dog.objects.get(id=id)
                usrdata = {
                    "id": data.id,
                    "name": data.name,
                    "age": data.age,
                    "created": data.created
                }
                msg['data'] = usrdata
                msg['signal'] = 1
            except:
                msg['signal'] = 2
        else:
            #print(UPDATE_ID)
            id = store['id']
            try:
                url = f'http://127.0.0.1:8000/api-auth/update/{id}/'
                print(url)
    
                response = requests.post(url, data={'name': name, 'age': age})
                print(response)
                print(response.json())
                print('here')
                msg['signal'] = 3
            except:
                msg['signal'] = 4
    return render(request, 'updateuser.html', msg)

def deleteUser(request):
    return render(request, 'delete.html')


def getUsersData():
    """ This function return all users in the database by simply calling the local API """
    url = 'http://127.0.0.1:8000/api-auth/view/'
    data = requests.get(url)
    data = data.json()
    
    return data