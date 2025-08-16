from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Car, Brand
from .forms import CarForm, BrandForm

def home(request):
    """Homepage - shows featured cars and recent additions"""
    featured_cars = Car.objects.filter(is_available=True).order_by('-date_added')[:6]
    recent_cars = Car.objects.order_by('-created_at')[:4]
    total_cars = Car.objects.count()
    total_brands = Brand.objects.count()
    
    context = {
        'featured_cars': featured_cars,
        'recent_cars': recent_cars,
        'total_cars': total_cars,
        'total_brands': total_brands,
    }
    return render(request, 'motors/home.html', context)

def car_list(request):
    """List all cars with filtering options"""
    cars = Car.objects.all().select_related('brand')
    brands = Brand.objects.all()
    
    # Filter by brand if specified
    brand_filter = request.GET.get('brand')
    if brand_filter:
        cars = cars.filter(brand__name__icontains=brand_filter)
    
    # Filter by availability
    available_only = request.GET.get('available')
    if available_only:
        cars = cars.filter(is_available=True)
    
    context = {
        'cars': cars,
        'brands': brands,
        'selected_brand': brand_filter,
        'available_only': available_only,
    }
    return render(request, 'motors/car_list.html', context)

def car_detail(request, car_id):
    """Show detailed information about a specific car"""
    car = get_object_or_404(Car, id=car_id)
    related_cars = Car.objects.filter(brand=car.brand).exclude(id=car.id)[:3]
    
    context = {
        'car': car,
        'related_cars': related_cars,
    }
    return render(request, 'motors/car_detail.html', context)

def add_car(request):
    """Form page to add a new car"""
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            messages.success(request, f'Car "{car.name}" added successfully!')
            return redirect('motors:car_detail', car_id=car.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CarForm()
    
    context = {
        'form': form,
        'title': 'Add New Car',
    }
    return render(request, 'motors/car_form.html', context)

def brand_list(request):
    """List all brands with their cars"""
    brands = Brand.objects.all().prefetch_related('cars')
    
    context = {
        'brands': brands,
    }
    return render(request, 'motors/brand_list.html', context)

def add_brand(request):
    """Form page to add a new brand"""
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            messages.success(request, f'Brand "{brand.name}" added successfully!')
            return redirect('motors:brand_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BrandForm()
    
    context = {
        'form': form,
        'title': 'Add New Brand',
    }
    return render(request, 'motors/brand_form.html', context)
