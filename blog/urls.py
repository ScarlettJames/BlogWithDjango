from django.urls import path
from .views import HomeView, AboutView, RegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView, name='blog.home'),
    path('about/', AboutView, name='blog.about'),
    path('register/', RegisterView, name='blog.register')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)