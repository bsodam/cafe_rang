from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cafes'
urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]