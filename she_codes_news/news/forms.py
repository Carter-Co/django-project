from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = {'title', 'author', 'pub_date', 'content'}
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'select a date','type':'date'}),
        }

class UserInfoForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()