from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import RecyclingCenter


class DetailRecyclingCenterView(DetailView):
    model = RecyclingCenter
    fields = ['data']

class ListRecyclingCenterView(ListView):
    model = RecyclingCenter
    fields = ['data']


detail_recycling_center_view = DetailRecyclingCenterView.as_view()
list_recycling_center_view = ListRecyclingCenterView.as_view()
