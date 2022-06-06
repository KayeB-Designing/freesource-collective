from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Resource

class Home(TemplateView):

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resources"] = Resource.objects.all()
        return context

class About(TemplateView):

    template_name = "about.html"

class LogIn(TemplateView):

    template_name = "login.html"

class Register(TemplateView):

    template_name = "register.html"

