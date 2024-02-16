from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import AddTask, EditTaskForms

def task_pending_list(request):
    task_pending = Task.objects.filter(status='pending')
    if request.method == 'POST':
        form = AddTask(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_pending_list')
        
    else:
        form = AddTask()
    return render(request, 'task/task_pending.html',
                  {'task_pending':task_pending, 'form':form})


def completed_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status =  'Completed'
    task.save()
    return redirect('task_pending_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_pending_list')

def postpone_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status =  'Postpone'
    task.save()
    return redirect('task_pending_list')

def edit_task(request, task_id):
    task = get_object_or_404(task, id=task_id)
    if request.method == 'POST':
        form = EditTaskForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            task.description = cd['task']
            task.category = cd['category']
            task.save()
            return redirect('task_pending_list')
    else:
        form = EditTaskForms(initial={'task':task.description, 'category':task.category})
    return render(request, 'task/edit_task.html', {'task':task, 'form':form})

def task_completed_list(request):
    task_completed = Task.objects.filter(status='completed')
    return render(request, 'task/task_completed.html', {'task_completed':task_completed})

def postpone_task_list(request):
    postpone_task = Task.objects.filter(status='postpone')
    return render(request, 'task/postpone_task.html', {'postpone_task':postpone_task})

def move_for_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'pending'
    task.save()
    return redirect('task_pending_list')