from django.db import models

# Create your models here.
class Dog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    #image = models.ImageField(upload_to='images/', null=True, default="Image not found")
    image = models.TextField(default="Image not found")
    location = models.TextField(default=None)
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=False)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.TextField(default=False)
    
    def __str__(self):
        self.id = id
        
class Like(models.Model):
    id = models.AutoField(primary_key=True)
    dog = models.ForeignKey("Dog", on_delete=models.CASCADE, default=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=False)
    liked = models.DateTimeField(auto_now_add=True)
    