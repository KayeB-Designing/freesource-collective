from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):

    def get(self, request):
        return HttpResponse("Freesource Library Collective Home Page")

class About(View):

    def get(self, request):
        return HttpResponse("Freesource Library Collective About Page")

class LogIn(View):

    def get(self, request):
        return HttpResponse("Freesource Library Collective Log In Page")

class Register(View):

    def get(self, request):
        return HttpResponse("Freesource Library Collective Registration Page")