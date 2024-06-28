from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            'body': forms.Textarea(attrs={ "placeholder": "Leave a comment!"})
        }

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "categories"]
        widgets = {
            'title': forms.Textarea(attrs={"placeholder": "Title"}),
            'body': forms.Textarea(attrs={"placeholder": "Text"})
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
