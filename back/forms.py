from django import forms
from .models import Comment, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','major','ad_year']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['classname','classkind','classcredits']

