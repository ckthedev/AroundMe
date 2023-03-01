from django.urls import path
from .views import UserHome,Profile,Bio,EditView

urlpatterns=[
    path("userhome/",UserHome.as_view(),name="userhome"),
    path("profile/",Profile.as_view(),name="profile"),
    path("bio/",Bio.as_view(),name="bio"),
    path("edit bio/",EditView.as_view(),name="edit bio"),
]