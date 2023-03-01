from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,UpdateView
from .forms import BioForm,EditForm
from .models import Bio,Edit
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

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
        messages.success(self.request,"Bio Added!")
        return super().form_valid(form)
    

class EditView(LoginRequiredMixin, UpdateView):
    model = Edit
    fields = ['bio', 'profile_pic']
    template_name = 'edit bio.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        edit_object, created = Edit.objects.get_or_create(user=self.request.user)
        return edit_object
        # try:
        #        return Edit.objects.get(user=self.request.user)
        # except Edit.DoesNotExist:
        #     return Edit.objects.create(user=self.request.user)

            

    def form_valid(self, form):
        form.instance.user = self.request.user
        edit_object = self.get_object()
        edit_object.bio = form.cleaned_data['bio']
        edit_object.profile_pic = form.cleaned_data['profile_pic']
        edit_object.save()
        return redirect('profile')
        
    
     
        
        
    
    
        

