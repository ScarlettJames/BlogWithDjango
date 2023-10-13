from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import todoListForm, WidgetOR, Styling
from .models import todoList
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
# @login_required(login_url='/account/login/')
# def todoListView(request):
#     model = todoList.objects.all()
#     context = {'items': model}
#     return render(request,'userhomepage.html',context)

class todoListView(LoginRequiredMixin,ListView):
    login_url = '/account/login/'
    model = todoList
    template_name = "userhomepage.html"
    context_object_name = 'items'

@login_required(login_url='/account/login/')
def todoListCreate(request):
    form = todoListForm(request.POST) if request.method == "POST" else todoListForm()
    if form.is_valid():
        get_data = form.clean()
        todoList.objects.create(**get_data)
        messages.success(request,message='Create Successful', fail_silently=True)
        return redirect('todolist.all')
    return render(request,'todoListCreate.html',{'form':form})

class todoListUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/account/login/'
    template_name = 'todoListUpdate.html'
    model = todoList
    form_class = todoListForm
    #fields = ['title', 'description', 'action']
    success_url = '/todolist/allitem/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,message='Update Successful!', fail_silently=True)
        return response
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = self.get_form_class()
    #     return context

# @login_required(login_url='/account/login/')
# def todoListUpdate(request, pk):
#     print(pk)
#     todolist = todoList.objects.get(pk=pk)
#     print(todolist.title)
#     if request.method == "POST":
#         form = todoListForm(request.POST)
#         if form.is_valid():
#             get_data = form.clean()
#             todolist.title = get_data['title']
#             todolist.description = get_data['description']
#             todolist.action = get_data['action']
#             todolist.save()
#             messages.success(request.message='Create Successful', fail_silently=True)
#             return redirect('todolist.all')
#     form = todoListForm()
#     form.fields['title'].widget = WidgetOR(forms.TextInput, Styling.title).createFormObj(value=todolist.title)
#     form.fields['description'].widget = WidgetOR(forms.Textarea, Styling.task).createFormObj(value=todolist.description)
#     return render(request,'todoListUpdate.html',{'form'=form})

# @login_required(login_url='/account/login/')
# def todoListDelete(request, pk):
#     if request.method == "POST":
#         item = todoList.objects.get(id=pk)
#         del_message = f'Title : {item.title} Deleted Success!'
#         messages.success(request, message=del_message,fail_silently=True)
#         item.delete()
#         return redirect('todolist.all')
#     return redirect('todolist.all')

class todoListDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    login_url = '/account/login/'
    model = todoList
    form_class = todoListForm
    template_name = 'todoListDelete.html'
    success_url = reverse_lazy('todolist.all')
    success_message = "Title: %(title)s is Delete Successful!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        context['form'] = self.form_class(instance=item)
        return context
    
    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(cleaned_data, title=self.object.title)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,message='Delete Successful!', fail_silently=True)
        return response