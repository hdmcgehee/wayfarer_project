
# ___________       HTTP RESPONSES   ______________________
from django.shortcuts import render, redirect
from django.http import HttpResponse

#      ___________       AUTH   ___________________________
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#  ___________     MODELS AND FORMS   _____________________ 
from .models import Profile, Post, City
from .forms import ProfileForm, CityForm, PostForm


# _________________________________________________________
# ___________________     USER     ________________________
# _________________________________________________________


# ________________   Sign Up Route    _____________________
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

# ________________    Profile Route  ______________________
@login_required
def profile(request):
    current_user = request.user
    id = current_user.id
    profile = Profile.objects.get(user=id)
    # POST METHOD
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile')
    # GET METHOD
    else:
        form = ProfileForm(instance=profile)
        context = {
            'profile': profile,
            'form': form
        }

        return render(request, 'registration/profile.html', context)

# _________________________________________________________
# ___________________     CITY     ________________________
# _________________________________________________________

# ________________   City Index Route  ____________________
@login_required
def city_index(request, city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    current_user = request.user
    id = current_user.id
    profile = Profile.objects.get(user=id)
    # POST METHOD
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.city_id = city_id
            new_post.profile_id = profile.id
            new_post.save()
        return redirect('city_index', city_id)
    # GET METHOD
    else:
        form = PostForm()
        context = {
            'city': city,
            'form': form,
            'cities': cities
        }
        return render(request, 'city/city.html', context)

# __________________________________________________________
# ___________________     POSTS     ________________________
# __________________________________________________________

# ________________     Post Detail    _____________________
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(id=post.profile_id)
    context = {
        'post': post, 
        'profile': profile
    }
    return render(request, 'post_detail.html', context)

# _________________     Post EDIT   _______________________
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    # POST METHOD
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            return redirect('city_index', post.city_id)
    # GET METHOD
    else:
        form = PostForm(instance = post)
        return render(request, 'post_edit.html', {'post': post, 'form': form})

# _______________      Post DELETE   ______________________
def post_delete(request, post_id):
  post = Post.objects.get(id = post_id)
  city_id = post.city_id
  Post.objects.get(id=post_id).delete()
  return redirect('city_index', city_id)


# _________________________________________________________
# ___________________     TBD     _________________________
# _________________________________________________________


# ________________    Home Route     ______________________ OLD
@login_required
def home(request):
    HttpResponse('home')

# ___________      City Detail Route   _____________________OLD
@login_required
def city_detail(request):
    return render(request, 'city/detail.html')