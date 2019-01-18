from django.shortcuts import render
from django.views.generic import ListView

from cafes.models import Cafe

# Create your views here.
class ListView(ListView):
    template_name = 'cafes/list.html'
    context_object_name = 'cafe_list'

    def get_queryset(self):
        return Cafe.objects.order_by('id')