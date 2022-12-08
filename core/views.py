from django.shortcuts import render, redirect
import requests
import json
from apiapp.models import Dog, User
from django.core import serializers
from django.core.files.storage import FileSystemStorage

# Create your views here.

BASE_ADDRESS = 'http://127.0.0.1:8000/media/'
#BASE_ADDRESS = 'https://dhananjaywho.pythonanywhere.com/media/'
FILE_SYSTEM = FileSystemStorage()

def login(request):
    """ This functions is used for validating user """
    msg = {}
    if request.session.get('user_id'):
        return redirect(home)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = User.objects.filter(email=email)
        for user in users:
            if user.password == password:
                request.session['user_id'] = user.id
                msg['status'] = 1
                return redirect(home)
        msg['status'] = 0
    return render(request, 'login.html')


def logout(request):
    del request.session['user_id']
    return redirect(login)

def register(request):
    """ This is the registeration page for new users """
    msg = {}
    if request.session.get('user_id'):
        return redirect(home)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {"username": username, "email": email, "password": password}
        url = 'http://127.0.0.1:8000/api-auth/register/'
        #url = 'https://dhananjaywho.pythonanywhere.com/api-auth/register/'
        try:
            reqdata = requests.post(url, data=data)
            print(reqdata)
            msg['saved'] = 1
            return redirect(login)
        except:
            msg['saved'] = 0
    return render(request, 'register.html')


def home(request):
    """ This is the root function for the core app """
    if request.session.get('user_id'):
        return render(request, 'index.html')
    return redirect(login)


def listUser(request):
    """ This function is used for viewing and searching the data elements """
    msg = {}
    msg['search'] = 0
    msg['signal'] = 0
    if request.session.get('user_id'):
        if request.method=='POST':
            """ We can also use the api to fetch this information. Here we have fetched from our databse."""
            search = request.POST.get('search')
            if search.isdigit():
                id = int(search)
                try:
                    data = Dog.objects.get(id=id)
                    usrdata = {
                        "id": data.id,
                        "name": data.name,
                        "description": data.description,
                        "image": BASE_ADDRESS+data.image,
                        "location": data.location,
                        "created": data.created
                    }
                    msg['search'] = 1
                    msg['filtereddata'] = usrdata
                except:
                    msg['search'] = 3
                
                #print(msg)
            else:
                name = search
                data = Dog.objects.filter(name=name)
                if not data:
                    msg['search'] = 3
                else:
                    usrdata = {}
                        
                    for ind,usr in enumerate(data):
                        lvl = {}
                        lvl['id'] = usr.id
                        lvl['name'] = usr.name
                        lvl['description'] = usr.description
                        lvl['image'] = BASE_ADDRESS+usr.image
                        lvl['location'] = usr.location
                        lvl['created'] = usr.created
                        usrdata[ind+1] = lvl
                    msg['search'] = 2
                    msg['filtereddata'] = usrdata
                    #print(msg['filtereddata'])
        try:
            data = getUsersData()
            print(data)
            for i in range(len(data)):
                data[i]['image'] = BASE_ADDRESS + data[i]['image']
            print(data)  
            msg['data'] = data
            msg['signal'] = 1
        except:
            msg['signal'] = 2

        return render(request, 'userlist.html', msg)
    return redirect(login)
 
       
def listSpecificUser(request):
    """ This was made with the view of creating a seperate profile for each instance """
    if request.session.get('user_id'):
        return render(request, 'listSpecificUser.html')
    return redirect(login)


def addUser(request):
    """ This function adds the new data to the database using the local API """
    msg = {}
    msg['added'] = 0
    if request.session.get('user_id'):
        #form = DogImageForm()
        if request.method=='POST':
            '''
            form = DogImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                print(form.data)
                msg['added'] = 1
            else:
                msg['added'] = 2
            '''
            name = request.POST.get('name')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            location = request.POST.get('location')
            user = User.objects.get(id=request.session['user_id'])
            imagename = FILE_SYSTEM.save(image.name, image)
            #image_url = FILE_SYSTEM.url(imagename)
            #print(imagename)
            url = 'http://127.0.0.1:8000/api-auth/add/'
            #url = 'https://dhananjaywho.pythonanywhere.com/api-auth/add/'
            try:
                data={"name": name, "description": description, "image": imagename, "location": location, "user": user.id}
                print(data)
                reqdata = requests.post(url, data=data)
                #print(reqdata) # Response code
                data = reqdata.json()
                #print(data)
                msg['added'] = 1
            except:
                msg['added'] = 2
        
        return render(request, 'add.html', msg)
    return redirect(login)


def updateUser(request):
    """ This function provides the connectivity to `updatingUser` function """
    msg = {}
    msg['search'] = -1
    if request.session.get('user_id'):
        if request.method=='POST':
            search = request.POST.get('search')
            
            if search:
                if search.isdigit():
                    usrid = int(search)
                    try:
                        data = Dog.objects.get(id=usrid)
                        usrdata = {
                            "id": data.id,
                            "name": data.name,
                            "description": data.description,
                            "image": BASE_ADDRESS+data.image,
                            "location": data.location,
                            "created": data.created
                        }
                        msg['search'] = 1
                        msg['filtereddata'] = usrdata
                    except:
                        msg['search'] = 3
                    
                else:
                    data = Dog.objects.filter(name=search)
                    if data:
                        usrdata = {}
                        for ind, usr in enumerate(data):
                            lvl = {}
                            lvl['id'] = usr.id
                            lvl['name'] = usr.name
                            lvl['description'] = usr.description
                            lvl['image'] = BASE_ADDRESS+usr.image
                            lvl['location'] = usr.location
                            lvl['created'] = usr.created
                            usrdata[ind+1] = lvl 
                        msg['filtereddata'] = usrdata 
                        print(usrdata)
                        msg['search'] = 2
                    else:
                        msg['search'] = 3
        #url = 'http://127.0.0.1:8000/api-auth/view/'
        try:
            data = getUsersData()
            filtered_data = []
            for dog in data:
                if dog['user'] == request.session['user_id']:
                    filtered_data.append(dog)
                    
            for i in range(len(filtered_data)):
                filtered_data[i]['image'] = BASE_ADDRESS + filtered_data[i]['image']
            
            msg['data'] = filtered_data
            print(filtered_data)
            msg['signal'] = 1
            '''
            data = response.text
            jsondata = json.loads(data)
            actualdata = jsondata[0]
            '''
            
        except:
            msg['signal'] = 2
            #print('\nError')
        
        return render(request, 'update.html',msg)
    return redirect(login)


def store_id(gid):
    """ This function is to store the id of the updating element """
    global store
    store['id'] = gid
store = {}

def updatingUser(request):
    """ This function actually takes the data to be updated and updates the data """
    msg = {}
    msg['signal'] = -1
    if request.session.get('user_id'):
        if request.method=='POST':
            id = request.POST.get('id')
                
            if id:
                store_id(id)
                try:
                    data = Dog.objects.get(id=id)

                    if data.user.id == request.session['user_id']:
                        usrdata = {
                            "id": data.id,
                            "name": data.name,
                            "description": data.description,
                            "image": BASE_ADDRESS+data.image,
                            "location": data.location,
                            "created": data.created
                        }
                        msg['data'] = usrdata
                        msg['signal'] = 1
                    else:
                        msg['signal'] = 3
                        return redirect('updateUser')
                except:
                    msg['signal'] = 2
            else:
                name = request.POST.get('name')
                description = request.POST.get('description')
                image = request.FILES.get('image')
                location = request.POST.get('location')
                upd_data = {}
                if name:
                    upd_data['name'] = name
                if description:
                    upd_data['description'] = description
                if image:
                    upd_data['image'] = image.name
                if location:
                    upd_data['location'] = location
                
                #upd_data = {"name": name, "description": description, "image":image.name, "location": location}
                #print(UPDATE_ID)
                id = store['id']
                dog = Dog.objects.get(id=id)
                prev_imgname = dog.image

                if upd_data.get('image'):
                    FILE_SYSTEM.delete(prev_imgname)
                    #print('deleted')
                    imagename = FILE_SYSTEM.save(image.name, image)
                    upd_data['image'] = imagename
                    #print('saved')
                else:
                    upd_data['image'] = prev_imgname
                
                if not upd_data.get('name'):
                    upd_data['name'] = dog.name
                if not upd_data.get('description'):
                    upd_data['description'] = dog.description
                if not upd_data.get('location'):
                    upd_data['location'] = dog.location
                try:
                    url = f'http://127.0.0.1:8000/api-auth/update/{id}/'
                    #url = f'https://dhananjaywho.pythonanywhere.com/api-auth/update/{id}'
                    response = requests.post(url, data=upd_data)
                    #print(response)
                    print(response.json())
                    data = Dog.objects.get(id=id)
                    msg['signal'] = 3
                except:
                    msg['signal'] = 4
        return render(request, 'updateuser.html', msg)
    return redirect(login)


def deleteUser(request):
    """ This function deletes a record from the database via the Local API and signals the termination of the process """
    msg = {}
    msg['signal'] = 1
    if request.session.get('user_id'):
        if request.method=='POST':
            search = request.POST.get('search')
            if search:
                msg['signal'] = -1
                if search.isdigit():
                    id = int(search)
                    try:
                        data = Dog.objects.get(id=id)
                        usrdata = {
                            "id": data.id,
                            "name": data.name,
                            "description": data.description,
                            "image": BASE_ADDRESS+data.image,
                            "location": data.location,
                            "created": data.created
                        }
                        msg['search'] = 1
                        msg['filtereddata'] = usrdata
                    except:
                        msg['search'] = 3
                else:
                    data = Dog.objects.filter(name=search)
                    if data:
                        usrdata = {}
                        for ind, usr in enumerate(data):
                            lvl = {}
                            lvl['id'] = usr.id
                            lvl['name'] = usr.name
                            lvl['description'] = usr.description
                            lvl['image'] = BASE_ADDRESS+usr.image
                            lvl['location'] = usr.location
                            lvl['created'] = usr.created
                            usrdata[ind+1] = lvl 
                        msg['filtereddata'] = usrdata 
                        #print(usrdata)
                        msg['search'] = 2
                    else:
                        msg['search'] = 3
            else:
                id = request.POST.get('id')
                try:
                    dog = Dog.objects.get(id=id)
                    if dog.user.id == request.session['user_id']:
                        url = f'http://127.0.0.1:8000/api-auth/delete/{id}/'
                        #url = f'https://dhananjaywho.pythonanywhere.com/api-auth/delete/{id}'
                        FILE_SYSTEM.delete(Dog.objects.get(id=id).image)
                        response = requests.delete(url)
                        print(response)
                        #print('Record and image deleted')
                        msg['signal'] = 2
                    else:
                        msg['signal'] = 4
                        return redirect(home)
                except:
                    msg['signal'] = 3
        
        url = 'http://127.0.0.1:8000/api-auth/view/'
        #url = 'https://dhananjaywho.pythonanywhere.com/api-auth/view/'
        response = requests.get(url)
        data = response.json()
        filtered_data = []
        for dog in data:
            if dog['user'] == request.session['user_id']:
                filtered_data.append(dog)
        for i in range(len(filtered_data)):
            filtered_data[i]['image'] = BASE_ADDRESS+filtered_data[i]['image']
        msg['data'] = filtered_data
        #print(data)
        
        return render(request, 'delete.html',msg)
    return redirect(login)


def getUsersData():
    """ This function return all users in the database by simply calling the local API """
    url = 'http://127.0.0.1:8000/api-auth/view/'
    #url = 'https://dhananjaywho.pythonanywhere.com/api-auth/view/'
    data = requests.get(url)
    data = data.json()
    
    return data
