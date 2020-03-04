from django.contrib import admin
from .models import Incidence

# Register your models here.
class IncidencesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

admin.site.register(Incidence, IncidencesAdmin)