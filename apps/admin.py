from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = 'slug',


class ProductImageInline(StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = 'slug',
    inlines = ProductImageInline,
