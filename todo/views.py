from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')

    return render(request, 'todo/task_list.html', {'tasks': tasks, 'form': form})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return render(request, 'todo/home.html')