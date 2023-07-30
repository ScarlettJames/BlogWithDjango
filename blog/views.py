from django.shortcuts import render
from .forms import Registeration
from .models import User

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
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST["password"]
    #     print(username, password)
    #     return render(request, 'register.html', {"form": form})
    # return render(request, 'register.html', {"form": form})
    if form.is_valid():
        cleaned_form = form.clean()
        User.objects.create(**cleaned_form)
        return render(request, 'home.html')
    return render(request, 'register.html', {"form": form})