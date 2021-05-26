from django.contrib import admin
from .models import CitizenInstances

# Register your models here.


admin.site.register(CitizenInstances, admin.ModelAdmin)