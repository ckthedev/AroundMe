from django.urls import path
from .views import *

urlpatterns=[
    path('Registration/',RegView.as_view(),name="Registration"),
    path('Login/',LogView.as_view(),name="Login")
]