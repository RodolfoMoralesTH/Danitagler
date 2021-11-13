from django.contrib import admin
from .models import Topic, Clase, Module, ModuleTask
# Register your models here.
admin.site.register(Clase)
admin.site.register(Topic)
admin.site.register(Module)
admin.site.register(ModuleTask)
