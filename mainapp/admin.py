from django.contrib import admin

from mainapp.models import ProductCategory, Product

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('image', 'category', 'description', ('price', 'quantity'))
    readonly_fields = ('description',)
    ordering = ('price',)
    search_fields = ('name',)
