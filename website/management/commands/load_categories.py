from django.core.management.base import BaseCommand
import csv
from website.models import Category

class Command(BaseCommand):
    help = "Load book categories from a CSV file"

    def handle(self, *args, **kwargs):
        file_path = "D:/Users/RISHAB/webprojec/boek/categories.csv"  # Update this path
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            #next(reader)  # Skip header
            for row in reader:
                print(f"Processing row: {row}")  # Debugging
                self.stdout.write(self.style.SUCCESS('Successfully loaded categories!'))
                if not row:  # Skip empty rows
                    continue

                Category.objects.get_or_create(name=row[0])
