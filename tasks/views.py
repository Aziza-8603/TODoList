from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'base.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:home')
    else:
        form = TaskForm()

    return render(request, 'add.html', {'form': form})


@login_required
def incomplete(request):
    tasks = Task.objects.filter(
        user=request.user,
        is_completed=False
    )
    return render(request, 'undone.html', {'tasks': tasks})


@login_required
def complete(request):
    tasks = Task.objects.filter(
        user=request.user,
        is_completed=True
    )
    return render(request, 'done.html', {'tasks': tasks})

@login_required
def status_changer(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('tasks:home')

# @login_required
# def status_changer(request, id):
#     task = get_object_or_404(Task, id=id, user=request.user)
#     task.completed = not task.completed
#     task.save()
#     return redirect('tasks:home')


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('tasks:home')