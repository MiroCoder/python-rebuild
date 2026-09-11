# Day 13 — Migrations + relationships

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )

    def __str__(self):
        return self.name


# Migration flow practiced:
# models.py changed
# -> python manage.py makemigrations
# -> python manage.py migrate
#
# For an existing table, category was first added with null=True,
# existing rows were backfilled, then null=True was removed.


# Relationship practice in Django shell:
# electronics = Category.objects.get(name="Electronics")
# laptop = Product.objects.get(name="Laptop")
#
# Forward relationship:
# laptop.category
# laptop.category.name
#
# Reverse relationship via related_name:
# electronics.products.all()
# electronics.products.filter(price__gt=100)
# electronics.products.count()
#
# Filter across relationship:
# Product.objects.filter(category__name="Electronics")
#
# Reassign relationship:
# accessories = Category.objects.get(name="Accessories")
# cable = Product.objects.get(name="Cable")
# cable.category = accessories
# cable.save()
