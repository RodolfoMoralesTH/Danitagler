from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# clase, user, topic

class Topic(models.Model):
    #name, description, classes
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Clase(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True )
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    #participants
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Module(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

class ModuleTask(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.TextField(null=True, blank=True)
    image = models.ImageField()
    pdf = models.FileField(null=True, blank=True)
