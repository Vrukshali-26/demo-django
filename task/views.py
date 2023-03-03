from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.

tasks = ['feed my cat', 'take my cat to walk']

def task(request):
    return render(request, "task/index.html", {
        "tasks": tasks
    })

class TaskForm(forms.Form):
    task_field = forms.CharField(max_length=100)

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('task/thanks.html')
    else:
        form = TaskForm()
    return render(request, "task/new.html", {"form": form})