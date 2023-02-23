from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView
from django.http import HttpResponse
from .forms import RegForm,LogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
# class Homepage(View):
#     def get(self,req,*args,**kwargs):
#         return render(req,"Homepage.html")
    
class Homepage(TemplateView):
    template_name="Homepage.html"





# class RegView(View):
#     def get(self,req,*args,**kwargs):
#         f=RegForm()  
#         return render(req,"Registration.html",{"form":f})
#     def post(self,req,*args,**kwargs):
#         f=RegForm(data=req.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(req,"User Registered SuccessFully")
#             return redirect("Homepage")
#         else:
#             messages.error(req,"reqistration Failed!")
#             return render(req,"Registration.html",{"form":f})
        
class RegView(CreateView):
    form_class=RegForm
    template_name="Registration.html"
    model=User
    success_url=reverse_lazy("Homepage")

class LogView(FormView):
    template_name="Login.html"
    form_class=LogForm
    def post(self,req,*args,**kwargs):
        f=LogForm(data=req.POST)
        if f.is_valid():
            us=f.cleaned_data.get("username")
            ps=f.cleaned_data.get("password")
            authenticate(req,username=us,password=ps)
            if User:
                login(req,User)
                messages.success(req," Login SuccessFull!!")
                return redirect("userhome")
            else:
                 messages.error(req,"Login Failed!!")
                 return render(req,"Login.html",{"form":f})


                #  dakdsfkjhdkjsfhkhdskjfh
        
