from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Place, Review
from .forms import ReviewForm

def dashboard(request):
    places = Place.objects.all()
    
    # Filter handling
    search_query = request.GET.get('search')
    state = request.GET.get('state')
    city = request.GET.get('city')
    min_rating = request.GET.get('min_rating')

    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if state:
        places = places.filter(state__iexact=state)
    if city:
        places = places.filter(city__iexact=city)
    if min_rating:
        places = [p for p in places if p.average_rating() >= float(min_rating)]

    context = {
        'places': places,
        'states': Place.objects.values_list('state', flat=True).distinct(),
        'cities': Place.objects.values_list('city', flat=True).distinct(),
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