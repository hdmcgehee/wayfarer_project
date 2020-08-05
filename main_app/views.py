from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile, Post, City
from .forms import ProfileForm, CityForm, PostForm

# Define the home view

@login_required
def home(request):
  HttpResponse('home')


def signup(request):
  error = None
  form = UserCreationForm()
  context = {
    'form': form,
    'error': error,
  }
  if request.method == 'POST':
    #create instance of form
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        print(user.id)
        ###
        user_profile = Profile.objects.create(user=user)
        user_profile.save()
        print(user_profile)

        # user_profile.save(commit=false)
        # user_profile.user(user)
        
        print('elif block hit')
        return redirect('signup')
    else:
      return redirect('signup')
  else:
    return render(request, 'home.html', context)

@login_required
def city_detail(request):
  return render(request, 'city/detail.html')

@login_required
def profile(request):
  current_user = request.user
  id = current_user.id
  profile = Profile.objects.get(user = id)
  if request.method == 'POST':
    form = ProfileForm(request.POST, instance = profile)
    if form.is_valid():
      profile = form.save()
      return redirect('profile')
  
  
  else:
    form = ProfileForm(instance = profile)

    context = {
      'profile': profile,
      'form': form
    }

    return render(request, 'registration/profile.html', context)

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  profile = Profile.objects.get(id=post.profile_id)
  
  return render(request, 'post_detail.html', {'post': post, 'profile': profile})