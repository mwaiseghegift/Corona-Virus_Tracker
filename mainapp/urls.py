from django.urls import path
from .views import (HomeView,
                    CountriesListView,
                    CountriesDetailView)

app_name = 'mainapp'

urlpatterns = [
    path('', HomeView, name='homepage'),
    path('countries', CountriesListView, name='countries'),
    path('countries/<int:pk>', CountriesDetailView, name="country_detail" )
]
