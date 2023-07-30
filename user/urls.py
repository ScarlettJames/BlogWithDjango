from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('registration/',RegisterView,name='blog.register'),
    path('login/',LoginView,name='blog.login'),
    path('logout/',LogoutView,name='blog.logout'),
]