from rest_framework import serializers
from apiapp.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age', 'created'] # or '__all__'