from django.shortcuts import render
from django.views.generic import View,CreateView,TemplateView

class UserHome(TemplateView):
    template_name="userhome.html"