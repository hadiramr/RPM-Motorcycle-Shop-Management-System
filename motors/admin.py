from django.contrib import admin

# Register your models here.

from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'founded_year', 'car_count', 'created_at']
    list_filter = ['country', 'founded_year']
    search_fields = ['name', 'country', 'description']
    ordering = ['name']
    
    def car_count(self, obj):
        return obj.cars.count()
    car_count.short_description = 'Number of Cars'

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model', 'year', 'price', 'fuel_type', 'is_available', 'date_added']
    list_filter = ['brand', 'year', 'fuel_type', 'transmission', 'is_available', 'date_added']
    search_fields = ['name', 'model', 'brand__name', 'description']
    list_editable = ['price', 'is_available']
    ordering = ['-date_added']
    date_hierarchy = 'date_added'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('brand', 'name', 'model', 'year', 'description')
        }),
        ('Technical Details', {
            'fields': ('fuel_type', 'transmission', 'engine_size', 'mileage')
        }),
        ('Pricing & Status', {
            'fields': ('price', 'is_available')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )
