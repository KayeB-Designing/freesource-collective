from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(TemplateView):

    template_name = "home.html"

class About(TemplateView):

    template_name = "about.html"

class LogIn(TemplateView):

    template_name = "login.html"

class Register(TemplateView):

    template_name = "register.html"