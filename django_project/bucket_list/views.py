from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .models import *
from .forms import *


def welcome(request):
    return render(request, 'bucket_list/welcome.html')

def tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'bucket_list/tasks.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {'form':form}
    return render(request, 'bucket_list/update.html', context)

def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('tasks')
    
    context = {'item':item}
    return render(request, 'bucket_list/delete.html', context)