from django.urls import path

urlpatterns = [
    path('', HomeView, name='blog.home'),
    path('about/', AboutView, name='blog.about'),
]