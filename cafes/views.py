from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cafes.models import Cafe

# Create your views here.
class ListView(ListView):
    template_name = 'cafes/list.html'
    context_object_name = 'cafe_list'

    def get_queryset(self):
        return Cafe.objects.order_by('id')

class DetailView(DetailView):
	model = Cafe
	# template_name = 'cafes/cafe_detail.html'

class ResultListView(ListView):
    template_name = 'cafes/results.html'
    context_object_name = 'cafe_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('search_keyword','')
        print("ResultListView called")
        print(search_keyword)
        return Cafe.objects.filter(cafe_name__contains=search_keyword)