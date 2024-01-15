from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="new task")
    # priority = forms.IntegerField(label="priority", min_value=1, max_value=5)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"tasks/index.html", {
        'tasks': request.session["tasks"]
    })

def add (request):
    if request.method == "POST":
        user_form = NewTaskForm(request.POST)
        if user_form.is_valid():
            new_task =user_form.cleaned_data['task']
            request.session["tasks"] += [new_task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else: 
            return render(request, 'tasks/add.html',{'form': user_form})
        

    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })

