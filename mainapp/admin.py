from django.contrib import admin
from .models import Country
# Register your models here.

admin.site.site_header="RETECH Corona Statistics"
admin.site.site_title="RETECH Corona Stats"


admin.site.register(Country)