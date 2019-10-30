from django.urls import path

from oscar.scans.views import add_scan_view

app_name = "scans"
urlpatterns = [path("", view=add_scan_view, name="add_scan")]
