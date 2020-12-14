from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'bucket_list/welcome.html')


@login_required(login_url='login')
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    
    if request.method == 'POST':
        form = TaskForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Successfully created!") 
            

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {'tasks':tasks, 'form':form}
    return render(request, 'bucket_list/tasks.html', context)



@login_required(login_url='login')
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated!") 
            return redirect('tasks')

    context = {'form':form}
    return render(request, 'bucket_list/update.html', context)


@login_required(login_url='login')
def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, "Successfully deleted!") 
        return redirect('tasks')
    
    context = {'item':item}
    return render(request, 'bucket_list/delete.html', context)