from django.contrib import admin
from .models import Category, Product, ProductImage, Review


class ProductImageInline(admin.TabularInline):
    """Inline pour les images supplémentaires des produits"""
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_filter = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount_percentage', 'stock', 'available', 'featured', 'created_at']
    list_filter = ['available', 'featured', 'category', 'created_at']
    list_editable = ['price', 'stock', 'available', 'featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Informations de base', {
            'fields': ('category', 'name', 'slug', 'description', 'image')
        }),
        ('Prix et stock', {
            'fields': ('price', 'discount_percentage', 'stock', 'available')
        }),
        ('Options', {
            'fields': ('featured',)
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'created_at']
    list_filter = ['created_at']
    search_fields = ['product__name', 'alt_text']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['product__name', 'user__username', 'comment']
    readonly_fields = ['created_at']
