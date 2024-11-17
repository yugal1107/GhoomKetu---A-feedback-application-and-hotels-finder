
# places/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Place(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    image = models.ImageField(upload_to='places/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        avg = self.reviews.aggregate(models.Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0

    def __str__(self):
        return self.name

class Review(models.Model):
    place = models.ForeignKey(
        Place, 
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s review for {self.place.name}"