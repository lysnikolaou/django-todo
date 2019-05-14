from django.shortcuts import render, redirect

from . import models


def index(request):
    return redirect('get_tasks')


def about(request):
    return render(request, 'impressum.html')


def get_tasks(request):
    context = {
        'tasks': models.Task.objects.all()
    }
    return render(request, 'homepage.html', context=context)


def add_task(request):
    if request.method == 'POST':
        new_task = models.Task.objects.create(
            text=request.POST.get('text', ''),
            deadline=request.POST.get('deadline', '1970-01-01'),
            progress=request.POST.get('progress', '0')
        )
        return redirect('get_tasks')
    return render(request, 'add.html')


def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    if request.method == 'POST':
        task.text = request.POST.get('text', '')
        task.deadline = request.POST.get('deadline', '1970-01-01')
        task.progress = request.POST.get('progress', '0')
        task.save()
        return redirect('get_tasks')
    else:
        return render(request, 'edit.html', context={'task': task})


def delete_task(request, id):
    if request.method == 'POST':
        task = models.Task.objects.get(pk=id)
        task.delete()
        return redirect('get_tasks')