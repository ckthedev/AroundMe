from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout,authenticate
from .forms import BioForm
from .models import Bio
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class UserHome(TemplateView):
    template_name="userhome.html"


class Profile(TemplateView):
    template_name="profile.html"    


class BioView(CreateView):
    form_class=BioForm
    template_name="bio.html"
    model=Bio
    success_url=reverse_lazy("profile")
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object = form.save()
        messages.success(self.request,"Bio Added!")
        return super().form_valid(form)
    
class EditView(UpdateView):
        form_class=BioForm
        model=Bio
        template_name="edit bio.html"
        success_url = reverse_lazy("profile")
        pk_url_kwarg="pk"
     
class ChangePasswordView(PasswordChangeView):
    template_name = 'change pswd.html'
    success_url = reverse_lazy('profile')     


        
    
    
        

