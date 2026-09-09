# Day 11 — Django Structure
# Request flow: project urls -> app urls -> view -> response

# products/views.py
from django.http import Http404, JsonResponse

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 40},
    {"id": 3, "name": "Monitor", "price": 300},
]


def product_list(request):
    return JsonResponse(products, safe=False)


def product_detail(request, product_id):
    try:
        product = next(item for item in products if item["id"] == product_id)
        data = {
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
        }
        return JsonResponse(data)
    except StopIteration:
        raise Http404("Product not found")


# products/urls.py
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.product_list),
#     path("<int:product_id>/", views.product_detail),
# ]

# backend/urls.py
# from django.contrib import admin
# from django.urls import include, path
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("products/", include("products.urls")),
# ]
