from django.contrib import admin
from .models import Book, Category,Rental
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "available_copies","owner"]
    list_filter = ["category"]
    search_fields = ["title", "author"]

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ["book", "renter", "rental_duration", "return_date"]