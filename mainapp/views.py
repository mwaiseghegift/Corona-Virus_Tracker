from django.shortcuts import render
import requests
from .models import Country

# Create your views here.

def HomeView(request, *args, **kwargs):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Kenya"}

    headers = {
        'x-rapidapi-key': "3309c51481msh3e38aacc1ee9fc3p1de04bjsn538e242cf931",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response'][0]
    print(data)
    context = {
        'new':data['cases']['new'],
        'active':data['cases']['active'],
        'critical':data['cases']['critical'],
        'recovered':data['cases']['recovered'],
        'deaths':data['deaths']['total'],
        'new_deaths':data['deaths']['new'],
        'total':data['cases']['total'],
        'date_updated':data['day'],
        'time_updated':data['time']
        
    }
    
    return render(request, 'index.html', context)

def CountriesListView(request, *args, **kwargs):

    countries = Country.objects.all()
    

    context = {
        'countries':countries,
        
    }
    return render(request, 'countries.html', context)
