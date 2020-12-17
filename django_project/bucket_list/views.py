from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def welcome(request):
    return render(request, 'bucket_list/welcome.html')



@login_required(login_url='login')
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Successfully created!")
            return redirect(instance.get_absolute_url())

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


@login_required(login_url='login')
def add_category(request):
    category = Category.objects.filter(creator=request.user)
    form = CategoryForm()

    
    if request.method == 'POST':
        print(form.is_valid())
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            instance1 = form.save(commit=False)
            instance1.creator = request.user
            instance1.save()
            messages.success(request, "Successfully created!") 
            

        return HttpResponseRedirect(instance1.get_absolute_url())

    context = {'category':category, 'form':form}
    return render(request, 'bucket_list/category.html', context)


@login_required(login_url='login')
def update_category(request, pk):
    task = Category.objects.get(id=pk)
    form = CategoryForm(instance=task)

    if request.method == "POST":

        form = CategoryForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated!") 
            return redirect('category')

    context = {'form':form}
    return render(request, 'bucket_list/update_category.html', context)


@login_required(login_url='login')
def delete_category(request, pk):
    item = Category.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, "Successfully deleted!") 
        return redirect('category')
    
    context = {'item':item}
    return render(request, 'bucket_list/delete_category.html', context)



@login_required(login_url='login')
def category(request, cat):
    tasks = Task.objects.filter(user=request.user)
    category_task = Task.objects.filter(category=cat.replace('-', ' '))
    return render(request, 'bucket_list/categories.html', {'tasks':tasks, 'cat':cat.title(), 'category_task':category_task})