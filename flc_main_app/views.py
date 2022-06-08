from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Resource, Comment, Resourcelist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class Home(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resources"] = Resource.objects.all()
        return context

class About(TemplateView):

    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class ResourceList(TemplateView):

    template_name = "resource_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resources"] = Resource.objects.all()
        name = self.request.GET.get("name")
        if name != None:
            context["resources"] = Resource.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["resources"] = Resource.objects.filter(user=self.request.user)
            context["header"] = "Resources"
        return context

class ResourceListList(TemplateView):

    template_name = "list_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lists"] = Resourcelist.objects.filter(creator=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class ResourceCreate(CreateView):
    model = Resource
    fields = ['name', 'image', 'link', 'habit_building', 'goal_setting', 'time_management', 'growth_mindset', 'general_pers_dev', 'type_book', 'type_video', 'type_podcast', 'type_worksheet', 'type_article', 'type_other']
    template_name = "resource_create.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ResourceCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('resource_detail', kwargs={'pk': self.object.pk})


class ResourceDetail(DetailView):
    model = Resource
    template_name = "resource_detail.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["lists"] = Resourcelist.objects.filter(creator=self.request.user)


@method_decorator(login_required, name='dispatch')
class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['name', 'image', 'link', 'habit_building', 'goal_setting', 'time_management', 'growth_mindset', 'general_pers_dev', 'type_book', 'type_video', 'type_podcast', 'type_worksheet', 'type_article', 'type_other']
    template_name = "resource_update.html"
    success_url = "/resources/"
    def get_success_url(self):
        return reverse('resource_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class ResourceDelete(DeleteView):
    model = Resource
    template_name = "resource_delete_confirmation.html"
    success_url = "/resources/"

class Register(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/register.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("resource_list")
        else:
            context = {"form": form}
            return render(request, "registration/register.html", context)

class CommentCreate(View):

    def post(self, request, pk):
        resource = Resource.objects.get(pk=pk)
        authorID = self.request.user
        body = request.POST.get("body")
        Comment.objects.create( authorID=authorID, resource=resource, body=body)
        return redirect('resource_detail', pk=pk)

# class CommentUpdate(UpdateView):
#     model = Comment
#     fields = ['comment_text']
#     template_name = "comment_update.html"
#     def get_success_url(self):
#         return reverse('/resources/<int:pk>/', kwargs={'pk': self.object.pk})

# class CommentDelete(DeleteView):
#     model = Comment
#     template_name = "comment_delete_confirmation.html"
#     success_url = "/resources/<int:pk>/"



# class ListCreate(CreateView):
#     model = ListList
#     fields = ['name', 'image', 'fav_list', 'habit_building', 'goal_setting', 'time_management', 'growth_mindset', 'general_pers_dev']
#     template_name = "list_create.html"
#     success_url = "/lists/"

class ResourceListCreate(CreateView):
    model = Resourcelist
    fields = ['name', 'image', 'resources', 'fav_list', 'habit_building', 'goal_setting', 'time_management', 'growth_mindset', 'general_pers_dev']
    template_name = "list_create.html"
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(ResourceListCreate, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('list_detail', kwargs={'pk': self.object.pk})


class ResourceListDetail(DetailView):
    model = Resourcelist
    template_name = "list_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resources"] = Resource.objects.all()
        return context

class ResourceListUpdate(UpdateView):
    model = Resourcelist
    fields = ['name', 'image', 'resources', 'fav_list', 'habit_building', 'goal_setting', 'time_management', 'growth_mindset', 'general_pers_dev']
    template_name = "list_update.html"
    def get_success_url(self):
        return reverse('list_detail', kwargs={'pk': self.object.pk})


class ResourceListDelete(DeleteView):
    model = Resourcelist
    template_name = "list_delete_confirmation.html"
    success_url = "/lists/"
# class ResourceListCreate(View):

#     def post(self, request, pk):
        
#         creator = self.request.user
#         name = request.POST.get("name")
#         image = request.POST.get("image")
#         resource = Resource.objects.get(pk=pk)
#         ResourceList.objects.create(creator=creator, name=name, image=image, resource=resource)
#         return redirect('artist_detail', pk=pk)

# class ResourceListDetail(DetailView):
#     model = ResourceList
#     template_name = "resource_detail.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["resources"] = Resource.objects.all()
#         # context["recipes"] = Recipe.objects.all()
#         # context["cookbooks"] = Cookbook.objects.all()
#         return context

class ResourcelistResourceAssoc(View):

    def get(self, request, pk, resource_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Resourcelist.objects.get(pk=pk).resources.remove(resource_pk)
        if assoc == "add":
            Resourcelist.objects.get(pk=pk).resources.add(resource_pk)
        return redirect('/lists/')

# class ResourcelistResourceAssoc(View):

#     def get(self, request, pk, resource_pk):
#         # get the query param from the url
#         assoc = request.GET.get("assoc")
#         if assoc == "remove":
#             # get the playlist by the id and
#             # remove from the join table the given resource_id
#             Resourcelist.objects.get(pk=pk).resources.remove(resource_pk)
#         if assoc == "add":
#             # get the playlist by the id and
#             # add to the join table the given resource_id
#             Resourcelist.objects.get(pk=pk).resources.add(resource_pk)
#         return redirect('lists')


class LogIn(TemplateView):

    template_name = "login.html"

# class Register(TemplateView):

#     template_name = "registration/register.html"