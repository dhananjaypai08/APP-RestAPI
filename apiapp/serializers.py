from rest_framework import serializers
from apiapp.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'created'] # or '__all__'