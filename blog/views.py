from django.shortcuts import render
from .forms import Registeration

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
    form = Registeration()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST["password"]
        print(username, password)
        return render(request, 'register.html', {"form": form})
    return render(request, 'register.html', {"form": form})