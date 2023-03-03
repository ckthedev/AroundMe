from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Bio(models.Model):
    dob=models.DateField()
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )

    gender=models.CharField(max_length=100,choices=options,default="Male")
    phone=models.IntegerField()
    status=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="user_profile_pictures",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="bio_user")



class Posts(models.Model):
    image=models.ImageField(upload_to="posted_images",null=True)
    caption=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="p_user")
    likes=models.ManyToManyField(User,related_name="liked_user")

class Comments(models.Model):
    comment=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="commented_user")
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="commented_post")