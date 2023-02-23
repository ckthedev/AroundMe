from django.urls import path
from .views import UserHome

urlpatterns=[
    path("userhome/",UserHome.as_view(),name="userpage")
]