from django.db import models
from django.urls import reverse
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    
    def get_absolute_url(self):    
        return reverse('mainapp:country_detail', kwargs={'name': self.name})
    
    def __str__(self):
        return self.name
