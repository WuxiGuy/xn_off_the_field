from django.contrib import admin
from .models import OffFieldApp

# Register your models here.
class OffFieldAppAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(OffFieldApp, OffFieldAppAdmin)