from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Place, Hotel, Review
from .forms import ReviewForm

def dashboard(request):
    view_type = request.GET.get('view', 'places')
    if view_type == 'hotels':
        items = Hotel.objects.all()
    else:
        items = Place.objects.all()

    # Filter handling
    search_query = request.GET.get('search')
    state = request.GET.get('state')
    city = request.GET.get('city')
    min_rating = request.GET.get('min_rating')
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if state:
        items = items.filter(state__iexact=state)
    if city:
        items = items.filter(city__iexact=city)
    if min_rating:
        items = [p for p in items if p.average_rating() >= float(min_rating)]
    context = {
        'items': items,
        'states': Place.objects.values_list('state', flat=True).distinct(),
        'cities': Place.objects.values_list('city', flat=True).distinct(),
        'view_type': view_type,
    }
    return render(request, 'places/dashboard.html', context)

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    reviews = place.reviews.all().order_by('-created_at')
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.place = place
            review.save()
            return redirect('place_detail', pk=pk)

    context = {
        'place': place,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'places/place_detail.html', context)

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    reviews = hotel.reviews.all().order_by('-created_at')
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hotel = hotel
            review.save()
            return redirect('hotel_detail', pk=pk)

    context = {
        'hotel': hotel,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'places/hotel_detail.html', context)