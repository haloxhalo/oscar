from django.contrib import admin
from .models import Company, SKU


class CompanyAdmin(admin.ModelAdmin):
    fields = ['data']

class SKUAdmin(admin.ModelAdmin):
    fields = ['data', 'company']


admin.site.register(SKU, SKUAdmin )
admin.site.register(Company, CompanyAdmin)

