from django.shortcuts import render
from .models import Topic, Clase, Module
# Create your views here.
#create, update, delete, login, logout, register
def home(request):
    clases = Clase.objects.all()
    context = { 'clases': clases}
    return render(request, 'base/home.html', context)

def Class(request, pk):
    class1 = Clase.objects.get(id=pk)
    modules = Module.objects.all()
    context = {'class1': class1, 'modules': modules}
    return render(request, 'base/clase.html', context)
