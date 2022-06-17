from rest_framework import serializers
from apiapp.models import Person

class PersonSerializer(serializers.ModelSerializer):
    #userid = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'created']