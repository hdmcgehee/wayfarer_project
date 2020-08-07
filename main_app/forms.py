from django import forms 
from .models import Profile, City, Post



#___________________________________PROFILE
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['city', 'image', 'display_name']



#___________________________________CITY
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country','image']



#___________________________________POST
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']