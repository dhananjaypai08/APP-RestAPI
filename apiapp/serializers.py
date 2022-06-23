from rest_framework import serializers
from apiapp.models import Dog
class DogSerializer(serializers.ModelSerializer):
    #userid = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    class Meta:
        model = Dog
        fields = '__all__' # or ['id', 'name', 'description', 'image', 'location','created']