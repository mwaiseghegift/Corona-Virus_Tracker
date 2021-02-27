from django.db import models
from django.urls import reverse
from PIL import Image
# Create your models here.

CONTINENTS = (
    ('Africa','Africa'),
    ('Europe','Europe'),
)


class Continent(models.Model):
    name = models.CharField(max_length=200)
    
    
    def get_absolute_url(self):
        return reverse("mainapp:category", kwargs={"name": self.name})
    
    def __str__(self):
        return self.name
class Region(models.Model):
    name = models.CharField(max_length=200)
    
    def get_absolute_url(self):
        return reverse("mainapp:region", kwargs={"name": self.name})
    
    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=200)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, 
                                 related_name="country_category",
                                 choices=CONTINENTS, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name="country_region",
                               blank=True, null=True)
    flag = models.ImageField(upload_to='images/country-flag', 
                             default='images/country-flag/hacker.jpg')
    
    def get_absolute_url(self):    
        return reverse('mainapp:country_detail', kwargs={'name': self.name})
    
    def __str__(self):
        return self.name


