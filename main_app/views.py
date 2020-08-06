from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile, Post, City
from .forms import ProfileForm, CityForm, PostForm


# ___________    Home Route  __________
@login_required
def home(request):
    HttpResponse('home')


# ___________    Sign Up Route  __________
def signup(request):
    error = None
    form = UserCreationForm()
    context = {
        'form': form,
        'error': error,
    }
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(user.id)

            user_profile = Profile.objects.create(user=user)
            user_profile.save()
            print(user_profile)

            print('elif block hit')
            return redirect('signup')
        else:
            return redirect('signup')
    else:
        return render(request, 'home.html', context)


# ___________    City Detail Route  __________
@login_required
def city_detail(request):
    return render(request, 'city/detail.html')


# ___________    City Index Route  __________
@login_required
def city_index(request, city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    current_user = request.user
    id = current_user.id
    profile = Profile.objects.get(user=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.city_id = city_id
            new_post.profile_id = profile.id
            new_post.save()

        return redirect('city_index', city_id)

    else:
        form = PostForm()

        context = {
            'city': city,
            'form': form,
            'cities': cities
        }
        return render(request, 'city/city.html', context)


# ___________    Profile Route  __________
@login_required
def profile(request):
    current_user = request.user
    id = current_user.id
    profile = Profile.objects.get(user=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

        context = {
            'profile': profile,
            'form': form
        }

        return render(request, 'registration/profile.html', context)


# ___________    Post Detail Route  __________
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(id=post.profile_id)

    return render(request, 'post_detail.html', {'post': post, 'profile': profile})


def post_edit(request, post_id):
  post = Post.objects.get(id=post_id)


  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      new_post = form.save()
      return redirect('city_index', post.city_id)

  else:
    form = PostForm(instance = post)
    return render(request, 'post_edit.html', {'post': post, 'form': form})

def post_delete(request, post_id):
  post = Post.objects.get(id = post_id)
  city = post.city_id

  Post.objects.get(id=post_id).delete()
  return redirect('city_index', city)