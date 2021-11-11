from django.shortcuts import render
from .models import Topic, Clase
# Create your views here.
#create, update, delete, login, logout, register
def home(request):
    return render(request, 'base/home.html')
