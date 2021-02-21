from django.urls import path
from .views import HomeView, CountriesListView

app_name = 'mainapp'

urlpatterns = [
    path('', HomeView, name='homepage'),
    path('countries', CountriesListView, name='countries'),
]
