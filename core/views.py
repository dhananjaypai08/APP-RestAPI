from django.shortcuts import render
import requests
import json
# Create your views here.

def home(request):
    return render(request, 'index.html')

def listUser(request):
    msg = {}
    msg['signal'] = 0
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
    return render(request, 'add.html')

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