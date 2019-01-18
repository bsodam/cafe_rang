from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cafes.models import Cafe, CafeKeyword

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

        queryset_cafe = Cafe.objects.filter(cafe_name__contains=search_keyword)

        keyword_results = CafeKeyword.objects.filter(cafe_keyword__contains=search_keyword).values("cafe_id")
        queryset_made = False
        if keyword_results:
            for keyword_result in keyword_results:
                if not queryset_made:
                    queryset_made = True
                    queryset_keyword = Cafe.objects.filter(id=keyword_result['cafe_id'])
                else:
                    queryset_keyword = Cafe.objects.filter(id=keyword_result['cafe_id']) | queryset_keyword

        if queryset_made:
            result = queryset_cafe | queryset_keyword
        else:
            result = queryset_cafe

        return result