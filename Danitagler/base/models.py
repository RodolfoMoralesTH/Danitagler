from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# clase, user, topic

class Topic(models.Model):
    #name, description, classes
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ModuleTask(models.Model):
    #add TIME, percentage
    module = models.ForeignKey('Module',on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    instructions = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Module(models.Model):
    #addTotalPercentage
    tasks = models.ManyToManyField(ModuleTask, related_name='tasks', blank=True)
    aula = models.ForeignKey('Clase', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Clase(models.Model):
    #addTotalPercentage
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True )
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    #participants
    name = models.CharField(max_length=200)
    modules = models.ManyToManyField(Module, related_name='modules', blank=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name




