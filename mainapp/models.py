from django.db import models
from django.urls import reverse
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class Continent(models.Model):
    name = models.CharField(max_length=200)
    
    
    def get_absolute_url(self):
        return reverse("mainapp:category", kwargs={"name": self.name})
    
    def __str__(self):
        return self.name
class Region(models.Model):
    name = models.CharField(max_length=200)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE,
                                  blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("mainapp:region", kwargs={"name": self.name})
    
    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=200)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, 
                                 related_name="country_category",
                                 null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name="country_region",
                               blank=True, null=True)
    flag = models.ImageField(upload_to='images/country-flag', 
                             default='images/country-flag/hacker.jpg')
    flag_thumbnail = ImageSpecField(source='flag',
                                    processors = [ResizeToFill(300,150)],
                                    format='JPEG',
                                    options = {'quality':100})
    
    def get_absolute_url(self):    
        return reverse('mainapp:country_detail', kwargs={'name': self.name})
    
    def __str__(self):
        return self.name


