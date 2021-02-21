from django.contrib import admin
from .models import Country
# Register your models here.

admin.site.header="RETECH Corona Statistics"

admin.site.register(Country)