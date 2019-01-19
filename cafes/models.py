from django.db import models

# Create your models here.
class Cafe(models.Model):
    cafe_name = models.CharField(max_length=30)
    cafe_address = models.CharField(max_length=100)
    cafe_phone = models.CharField(max_length=30)
    cafe_opening_hours = models.CharField(max_length=100, blank=True)
    cafe_menu = models.TextField(blank=True)
    # cafe_image = models.ImageField(blank=True)

    def __str__(self):
        return self.cafe_name

class CafeKeyword(models.Model):
    cafe_id = models.PositiveIntegerField()
    cafe_keyword = models.CharField(max_length=30)

    # def __str__(self):
    #     return [self.cafe_id, self.cafe_keyword]

    # fieldsets = [
    #     ('cafe_id', {'fields': ['cafe_id']}),
    #     ('cafe_keyword', {'fields': ['cafe_keyword']}),
    # ]