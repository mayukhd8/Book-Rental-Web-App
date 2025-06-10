from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date
from django.utils import timezone
from decimal import Decimal


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"  # Fix admin panel pluralization

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # For rental pricing
    owner = models.ForeignKey(User, related_name='owned_books', on_delete=models.CASCADE)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)  # Add this line for the image field

    def calculate_rental_price(self, duration_months):
        """
        Calculate rental price based on book price and duration.
        """
        price = (self.price)
        if price > 500:
            if duration_months == 1:
                return price - (price * Decimal(0.03))  # 3% for 1 month
            elif duration_months == 3:
                return price - (price * Decimal(0.05))  # 5% for 3 months
            elif duration_months == 6:
                return price - (price * Decimal(0.07))  # 7% for 6 months
            elif duration_months == 9:
                return price -(price * Decimal(0.11))  # 11% for 9 months
        else:
            # Same percentage logic for books priced under 500
            if duration_months == 1:
                return price - (price * Decimal(0.15))  # 3% for 1 month
            elif duration_months == 3:
                return price - (price * Decimal(0.20))  # 5% for 3 months
            elif duration_months == 6:
                return price - (price * Decimal(0.25))  # 7% for 6 months
            elif duration_months == 9:
                return price - (price * Decimal(0.30))

        return 0  # Default if no matching duration


    def __str__(self):
        return self.title

RENTAL_CHOICES = (
    (1, '1 Month'),
    (3, '3 Months'),
    (6, '6 Months'),
    (9, '9 Months'),
)

class Rental(models.Model):
    book = models.ForeignKey(Book, related_name='rentals', on_delete=models.CASCADE)
    renter = models.ForeignKey(User, related_name='rented_books', on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now_add=True)
    rental_duration = models.IntegerField(choices=RENTAL_CHOICES, default=1)  # Duration in months
    return_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    total_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        # Automatically calculate return date based on rental duration
        if not self.return_date:
            self.rental_date = timezone.now()

        self.return_date = self.rental_date + timedelta(days=30 * self.rental_duration)
        super(Rental, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} rented by {self.renter.username} for {self.rental_duration} month(s)"