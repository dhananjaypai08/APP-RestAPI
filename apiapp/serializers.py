from rest_framework import serializers
from apiapp.models import Dog, User, Like
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
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'