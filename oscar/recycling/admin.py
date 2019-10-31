from django.contrib import admin
from .models import RecyclingCenter


class RecyclingCenterAdmin(admin.ModelAdmin):
    fields = ['data']


admin.site.register(RecyclingCenter, RecyclingCenterAdmin)

