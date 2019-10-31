from django.urls import path

from oscar.products.views import detail_company_view, list_company_view, detail_sku_view, list_sku_view

app_name = "products"
urlpatterns = [path("detail_company/<int:pk>/", view=detail_company_view, name="detail_company"),
    path("list_company/", view=list_company_view, name="list_company"),
    path("detail_sku/<int:pk>/", view=detail_sku_view, name="detail_sku"),
    path("list_sku/", view=list_sku_view, name="list_sku")
]
