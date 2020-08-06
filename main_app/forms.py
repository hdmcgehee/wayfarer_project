from django import forms 
from .models import Profile, City, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['city', 'image', 'display_name']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country','image']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']