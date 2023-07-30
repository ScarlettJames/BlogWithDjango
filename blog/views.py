from django.shortcuts import render
from .forms import Registeration
from django.contrib.auth.models import User

# Create your views here.
def HomeView(request):
    context = {
        'title' : 'Home',
        'name' : 'Scarlett',
        'job' : 'Web developer',
        'age' : 18,
        'appearence' : 'handsome',
        'skills' : ['HTML', 'CSS', 'Javascript', 'Python', 'Java', 'PHP']
    }
    return render(request, 'home.html', context=context)

def AboutView(request):
    return render(request, 'about.html')

def RegisterView(request):
    form = Registeration(request.POST)
    if form.is_valid():
        cleaned_form = form.clean()
        User.objects.create(**cleaned_form)
        return render(request, 'home.html')
    return render(request, 'register.html', {"form": form})