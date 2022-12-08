from rest_framework import serializers
from apiapp.models import Dog, User
from django import forms 

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__' # or ['id', 'name', 'description', 'image', 'location','created']
    
'''
class DogImageForm(forms.ModelForm):
    
    class Meta:
        model = Dog
        fields = ['id', 'name', 'description', 'image', 'location']
'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'