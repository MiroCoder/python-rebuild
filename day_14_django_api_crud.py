# Day 14 — Django API mini-project: manual CRUD

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Product


@csrf_exempt
def product_list(request):
    if request.method == "GET":
        data = list(Product.objects.values("id", "name", "price", "stock"))
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)

        category = get_object_or_404(Category, id=data["category_id"])

        product = Product.objects.create(
            name=data["name"],
            price=data["price"],
            stock=data["stock"],
            category=category,
        )

        response_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category.name,
        }
        return JsonResponse(response_data, status=201)


@csrf_exempt
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "GET":
        data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category.name,
        }
        return JsonResponse(data)

    if request.method == "PATCH":
        data = json.loads(request.body)

        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.stock = data.get("stock", product.stock)
        product.save()

        response_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category.name,
        }
        return JsonResponse(response_data)

    if request.method == "DELETE":
        product.delete()
        return HttpResponse(status=204)


# URL mapping used:
# path("", views.product_list)
# path("<int:product_id>/", views.product_detail)
#
# CRUD covered manually:
# GET    /products/      -> list
# POST   /products/      -> create
# GET    /products/<id>/ -> retrieve
# PATCH  /products/<id>/ -> partial update
# DELETE /products/<id>/ -> delete
#
# Raw Django JSON flow:
# request.body -> json.loads(...) -> Python dict -> ORM -> JsonResponse
#
# csrf_exempt was used here only for the raw learning exercise.
# DRF will handle request parsing/auth/API behavior differently later.
