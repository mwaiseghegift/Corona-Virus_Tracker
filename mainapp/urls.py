from django.urls import path
from .views import HomeView, Countries

app_name = 'mainapp'

urlpatterns = [
    path('', HomeView, name='homepage'),
    path('countries', Countries, name='countries'),
]
