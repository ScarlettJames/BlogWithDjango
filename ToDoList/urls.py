from django.urls import path
from .views import todoListView, todoListCreate, todoListUpdate, todoListDelete

urlpatterns = [
    path('',todoListView.as_view()),
    path('allitem/',todoListView.as_view(),name='todolist.all'),
    path('new/', todoListCreate,name='todolist.new'),
    path('item/update/<int:pk>/', todoListUpdate.as_view(), name='todoList.update'),
    path('item/delete/<int:pk>/', todoListDelete.as_view(), name='todoList.delete'),
]