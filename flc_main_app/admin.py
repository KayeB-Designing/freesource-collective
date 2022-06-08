from django.contrib import admin
from .models import Resource, Comment, Resourcelist

admin.site.register(Resource)
admin.site.register(Resourcelist)
admin.site.register(Comment)
