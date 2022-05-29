from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def home(request):
    universe = Task.objects.all()
    if request.method =='POST':
        if request.POST['task'] != '':
            place = Task(task = request.POST['task'])
            place.save()
        else:
            pass
    return render(request, 'doapp/index.html',{'unique': universe})


def delete(request, pk):
    universe = Task.objects.get(id = pk)
    universe.delete()
    return redirect('home')

