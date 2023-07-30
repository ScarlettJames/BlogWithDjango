from django.shortcuts import render

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