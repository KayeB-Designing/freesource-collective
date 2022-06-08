from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    habit_building = models.BooleanField(default=False)
    goal_setting = models.BooleanField(default=False)
    time_management = models.BooleanField(default=False)
    growth_mindset = models.BooleanField(default=False)
    general_pers_dev = models.BooleanField(default=False)
    verified_download = models.BooleanField(default=False)
    type_book = models.BooleanField(default=False)
    type_video = models.BooleanField(default=False)
    type_podcast = models.BooleanField(default=False)
    type_worksheet = models.BooleanField(default=False)
    type_article = models.BooleanField(default=False)
    type_other = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Comment(models.Model):

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="comments")
    authorID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.body

class Resourcelist(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=250)
    resources = models.ManyToManyField(Resource)
    fav_list = models.BooleanField(default=False)
    habit_building = models.BooleanField(default=False)
    goal_setting = models.BooleanField(default=False)
    time_management = models.BooleanField(default=False)
    growth_mindset = models.BooleanField(default=False)
    general_pers_dev = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

