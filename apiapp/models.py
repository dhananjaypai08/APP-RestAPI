from django.db import models

# Create your models here.
class Dog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    #image = models.ImageField(upload_to='images/', null=True, default="Image not found")
    image = models.TextField(default="Image not found")
    location = models.TextField(default=None)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        self.id = id