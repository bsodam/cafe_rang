from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.apps import apps


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {'username': request.user.username}
        return render(request, 'index.html', context=context)


class AboutView(TemplateView):
    template_name = "about.html"

class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = '/registered'

class RegisterdView(TemplateView):
    template_name = 'registration/registered.html'