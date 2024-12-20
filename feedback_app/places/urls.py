from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
]