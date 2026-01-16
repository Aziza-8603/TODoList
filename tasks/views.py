from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# def home(request):
#     # tasks = Task.objects.all()
#     # context = {'tasks': tasks}
#     return render(request, 'base.html')

# def status_changer(request, id):
#     task = Task.objects.filter(id=id).update(status=True)
#     return redirect('home')

# from django.shortcuts import render, redirect
# from .models import Task

def home(request):
    return render(request, 'base.html')


def incomplete(request):
    tasks = Task.objects.filter(is_completed=False)
    return render(request, 'undone.html', {'tasks': tasks})


def complete(request):
    tasks = Task.objects.filter(is_completed=True)
    return render(request, 'done.html', {'tasks': tasks})


def status_changer(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('tasks:incompleted')

# def delate_task(request, id):
#     Task.objects.filter(id=id)
#     return redirect('complete')


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasks:completed')

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})
    
# def incomplete(request):
#     tasks = Task.objects.filter(status=False)
#     context = {'tasks': tasks}
#     return render (request, 'undone.html', context)

# def complete(request):
#     tasks = Task.objects.filter(is_completed=True)
#     return render(request, 'done.html', {'tasks': tasks})

# def incomplete(request):
#     tasks = Task.objects.filter(is_completed=False)
#     return render(request, 'undone.html', {'tasks': tasks})
