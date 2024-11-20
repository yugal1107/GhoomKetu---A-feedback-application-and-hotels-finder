from django.contrib import admin
from .models import Place, Hotel, Review

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'price', 'average_rating']
    list_filter = ['state', 'city']
    search_fields = ['name', 'description']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'price', 'average_rating']
    list_filter = ['state', 'city']
    search_fields = ['name', 'description']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['place', 'hotel', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user', 'text']