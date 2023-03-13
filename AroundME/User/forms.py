from django import forms
from .models import Bio,Posts,Comments

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["image","caption"]
        widgets={
            "image":forms.FileInput(),
            "caption":forms.TextInput(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]  
        widgets={
            "Comments":forms.Textarea(attrs={"class":"form-control"})
        }         

