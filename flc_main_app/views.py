from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Resource
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resources"] = Resource.objects.all()
        # name = self.request.GET.get("name")
        # if name != None:
        #     context["resources"] = Resource.objects.filter(
        #         name__icontains=name, user=self.request.user)
        #     context["header"] = f"Searching for {name}"
        # else:
        #     context["resources"] = Resource.objects.filter(user=self.request.user)
        #     context["header"] = "Resources"
        return context

class About(TemplateView):

    template_name = "about.html"

class LogIn(TemplateView):

    template_name = "login.html"

class Register(TemplateView):

    template_name = "register.html"

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

@method_decorator(login_required, name='dispatch')
class ResourceCreate(CreateView):
    model = Resource
    fields = ['name', 'image']
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

@method_decorator(login_required, name='dispatch')
class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['name', 'image']
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
