from django.shortcuts import render
from django.views.generic import View,CreateView,TemplateView
from .forms import BioForm
from .models import Bio
from django.urls import reverse_lazy
from django.contrib import messages

class UserHome(TemplateView):
    template_name="userhome.html"


class Profile(TemplateView):
    template_name="profile.html"    


class Bio(CreateView):
    form_class=BioForm
    template_name="bio.html"
    model=Bio
    success_url=reverse_lazy("profile")
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object = form.save()
        messages.success(self,request,"Bio Added!")
        return super().form_valid(form)
        

