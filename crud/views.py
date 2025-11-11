from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list_and_create(r):
    if r.method == 'POST':
        form = TaskForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = TaskForm()
    #tasks = Task.objects.all()
    complate_tasks = Task.objects.filter(is_completed=True)
    incomplete_tasks = Task.objects.filter(is_completed=False)

    return render(r,'task_list.html',{
        'form':form,
        'complete_tasks':complate_tasks,
        'incomplete_tasks':incomplete_tasks
    })