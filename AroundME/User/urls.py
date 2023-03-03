from django.urls import path
from .views import UserHome,Profile,BioView,EditView,ChangePasswordView

urlpatterns=[
    path("userhome/",UserHome.as_view(),name="userhome"),
    path("profile/",Profile.as_view(),name="profile"),
    path("bio/",BioView.as_view(),name="bio"),
    path("edit bio/<int:pk>",EditView.as_view(),name="edit bio"),
    path("change pswd/",ChangePasswordView.as_view(),name="change pswd"),
]