from django.shortcuts import render
from django.views.generic import CreateView
from .models import Scan


class AddScanView(CreateView):
    model = Scan


add_scan_view = AddScanView.as_view()
