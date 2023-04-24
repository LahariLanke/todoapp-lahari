from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

