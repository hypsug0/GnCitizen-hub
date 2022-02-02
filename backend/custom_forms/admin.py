from django.contrib import admin

from .models import CustomForm

# Register your models here.


admin.site.register(CustomForm, admin.ModelAdmin)
