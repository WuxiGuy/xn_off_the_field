from django.contrib import admin
from .models import OffFieldApp

# Register your models here.
'''
Initialize the information that needs to be displayed in admin website
'''
class OffFieldAppAdmin(admin.ModelAdmin):
    list_display = ('xx', 'xx', 'xx')

admin.site.register(OffFieldApp, OffFieldAppAdmin)