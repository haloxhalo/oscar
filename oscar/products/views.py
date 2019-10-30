from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Company, SKU


class DetailCompanyView(DetailView):
    model = Company
    fields = ['data']


class ListCompanyView(ListView):
    model = Company
    fields = ['data']


class DetailSKUView(DetailView):
    model = SKU
    fields = ['data','company']


class ListSKUView(ListView):
    model = SKU
    fields = ['data','company']


detail_company_view = DetailCompanyView.as_view()
list_company_view = ListCompanyView.as_view()
detail_sku_view = DetailSKUView.as_view()
list_sku_view = ListSKUView.as_view()

