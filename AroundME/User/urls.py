from django.urls import path
from .views import UserHome,Profile

urlpatterns=[
    path("userhome/",UserHome.as_view(),name="userhome"),
    path("profile/",Profile.as_view(),name="profile")
]