from django.contrib import admin
from .models import Country, Region, Continent
# Register your models here.

admin.site.site_header="RETECH Corona Statistics"
admin.site.site_title="RETECH Corona Stats"





admin.site.register(Continent)
admin.site.register(Region)
admin.site.register(Country)