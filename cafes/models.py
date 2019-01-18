from django.db import models

# Create your models here.
class Cafe(models.Model):
    cafe_name = models.CharField(max_length=30)
    cafe_address = models.CharField(max_length=100)
    cafe_phone = models.CharField(max_length=30)
    cafe_opening_hours = models.CharField(max_length=100, blank=True)
    cafe_menu = models.TextField(blank=True)
    # cafe_image = models.ImageField(blank=True)
