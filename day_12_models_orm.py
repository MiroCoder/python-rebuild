# Day 12 — Models + ORM

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


# Core ORM practice used in Django shell:
# Product.objects.create(name="Laptop", price=1200, stock=2)
# Product.objects.all()
# Product.objects.get(id=1)
# Product.objects.filter(price__gt=100)
# Product.objects.filter(stock__gt=0)
# Product.objects.filter(price__lte=100)
# Product.objects.order_by("price")
# Product.objects.order_by("-price")
# Product.objects.filter(stock__gt=0).order_by("price")
# Product.objects.filter(price__gt=50).order_by("-price")
# Product.objects.filter(stock=0).exists()
# Product.objects.filter(price__gt=100).count()
#
# Update:
# product = Product.objects.get(id=1)
# product.price = 1300
# product.save()
#
# Delete:
# product.delete()


# ORM-backed views used at the end of Day 12:
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
#
# def product_list(request):
#     data = list(Product.objects.values("id", "name", "price", "stock"))
#     return JsonResponse(data, safe=False)
#
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     data = {
#         "id": product.id,
#         "name": product.name,
#         "price": product.price,
#         "stock": product.stock,
#     }
#     return JsonResponse(data)
