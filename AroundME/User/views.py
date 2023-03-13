from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout,authenticate
from .forms import BioForm,PostForm,CommentForm
from .models import Bio,Posts,Comments
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class UserHome(CreateView):
    template_name="userhome.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("userhome")
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,'Post Uploaded')
        self.object=form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.all().order_by('-datetime')
        context["cform"]=CommentForm()
        context["comments"]=Comments.objects.all()
        return context
    
def Addcomment(request, *args, **kwargs):
    if request.method == "POST":
        cid = kwargs.get("cid")
        post = Posts.objects.get(id=cid)
        user = request.user
        cmnt = request.POST.get("comment")
        Comments.objects.create(comment=cmnt, user=user, post=post)
        return redirect("userhome")
def addlike(request,*args,**kwargs):
    pid=kwargs.get("pid")
    post=Posts.objects.get(id=pid) 
    user=request.user
    post.likes.add(user)
    post.save()
    return redirect("userhome")   


    
class Profile(TemplateView):
    template_name="profile.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.filter(user=self.request.user).order_by('-datetime')
        return context
    
class MyPostView(TemplateView):
    template_name="post.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.filter(user=self.request.user)
        return context
    
class PostEditView(UpdateView):
    model=Posts
    form_class=PostForm
    template_name="edit post.html"
    success_url=reverse_lazy("profile")
    pk_url_kwarg="pk"

class PostDeleteView(View):
    def get (self,req,*args,**kwargs):
        id=kwargs.get("pk")
        posts=Posts.objects.get(id=id)
        posts.delete()
        messages.success(req,"staff Removed")
        return redirect("userhome")   

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



    
        

