from django.db import models
# from datetimeutc.fields import DateTimeUTCField
from django.contrib.auth.models import User

# Create your models here.

# --- PROFILE MODEL
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, default='default city')
    image = models.CharField(max_length=1000, default='default_image.jpg')
    display_name = models.CharField(max_length=100, default='display name')
    

#  --- CITY MODEL
class City(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

# --- POST MODEL
class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    # date = models.DateTimeUTCField('Post Date') /// crashed the server




