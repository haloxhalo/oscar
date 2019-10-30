from django.shortcuts import render
from django.views.generic import CreateView
from .models import Scan


class CreateDetailView(CreateView):
    model = Scan
