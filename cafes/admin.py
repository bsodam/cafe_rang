from django.contrib import admin

# Register your models here.
from cafes.models import Cafe, CafeKeyword

admin.site.register(Cafe)
admin.site.register(CafeKeyword)