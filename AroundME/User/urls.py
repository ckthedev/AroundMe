from django.urls import path
from .views import UserHome,Profile,BioView,EditView,ChangePasswordView,MyPostView,PostEditView,PostDeleteView

urlpatterns=[
    path("userhome/",UserHome.as_view(),name="userhome"),
    path("profile/",Profile.as_view(),name="profile"),
    path("bio/",BioView.as_view(),name="bio"),
    path("edit bio/<int:pk>",EditView.as_view(),name="edit bio"),
    path("edit post/<int:pk>/",PostEditView.as_view(),name="edit post"),
    path("post delete/<int:pk>/",PostDeleteView.as_view(), name="post delete"),
    path("change pswd/",ChangePasswordView.as_view(),name="change pswd"),
    path("post/",MyPostView.as_view(),name="post"),
]