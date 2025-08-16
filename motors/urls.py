from django.urls import path
from . import views

app_name = 'motors'

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    
    # Car pages
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/add/', views.add_car, name='add_car'),
    
    # Brand pages
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/add/', views.add_brand, name='add_brand'),
]
