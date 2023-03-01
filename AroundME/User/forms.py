from django import forms
from .models import Bio,Edit

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Edit
        exclude=["user"]
        fields = ['bio', 'profile_pic']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }