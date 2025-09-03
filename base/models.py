from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # if user is deleted, set host to null
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True) # if topic is deleted, set topic to null
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) # many to many relationship with user, blank means its not required
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-updated', '-created'] # latest updated or created will be at the top

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # delete all the message of that user if user is deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # delete all the message of that room if room is deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ['-updated', '-created'] # latest updated or created will be at the top

    def __str__(self):
        return self.body[0:50] # first 50 char

    