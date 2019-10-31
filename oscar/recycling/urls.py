from django.urls import path

from oscar.recycling.views import detail_recycling_center_view, list_recycling_center_view 

app_name = "recycling"
urlpatterns = [
        path("center_detail/<int:pk>/", view=detail_recycling_center_view, name="detail_recycling_center_view"),
        path("center_list/", view=list_recycling_center_view, name="list_recycling_center_view"),
]
