from django.shortcuts import render
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def course(request):
    course_list = Course.objects.all()
    return render(request, 'course.html', {'course' : course_list})

def professor(request):
    professor_list = Professor.objects.all()
    return render(request, 'professor.html', {'professor' : professor_list})

def alumn(request):
    alumn_list = Alumn.objects.all()
    return render(request, 'alumn.html', {'alumn' : alumn_list})

def updateForm(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
        name = info['first_name']
        surname = info['last_name']
        age = info['age']
        alumn = Alumn(first_name=name, last_name=surname, age=age)
        alumn.save()
        return render(request, 'index.html')
    else:
        form = UpdateForm()
    return render(request, 'updateForm.html', {'form': form})