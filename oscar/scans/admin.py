from django.contrib import admin
from .models import Scan


class ScansAdmin(admin.ModelAdmin):
    fields = ['data']


admin.site.register(Scan, ScansAdmin)

