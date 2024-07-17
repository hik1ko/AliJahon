from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.utils.html import format_html

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
    list_display = 'name', 'price', 'category', 'image_photo', 'is_exists'

    @admin.display(empty_value='?')
    def image_photo(self, obj):
        photo = obj.images.first().image.url
        return format_html("<img src='{}' style='width:50px'/>", photo)

    @admin.display(empty_value='?')
    def is_exists(self, obj):
        if obj.quantity > 0:
            return format_html()
        else:
            return format_html()
