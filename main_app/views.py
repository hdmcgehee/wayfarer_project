
# ___________       HTTP RESPONSES   ______________________
from django.shortcuts import render, redirect
from django.http import HttpResponse

#      ___________       AUTH   ___________________________
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#  ___________     MODELS AND FORMS   _____________________ 
from .models import Profile, Post, City, Comment
from .forms import ProfileForm, CityForm, PostForm, CommentForm


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
            context['error'] = 'username taken'
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)




# ________________    About Route  ______________________
def about(request):

    return render(request, 'about.html')




# ________________    Profile Route  ______________________
@login_required
def profile(request, profile_id):
    current_user = request.user
    id = current_user.id
    current_profile = Profile.objects.get(user=id)
    this_profile = Profile.objects.get(id = profile_id)
    # POST METHOD
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            current_profile = form.save()
            return redirect('profile', profile_id)
    # GET METHOD
    else:
        form = ProfileForm(instance=current_profile)
        context = {
            'current_profile': current_profile,
            'this_profile': this_profile,
            'form': form
        }

        return render(request, 'registration/profile.html', context)


# ________________   User Profile Route  ____________________

@login_required
def user_profile(request):
    current_user = request.user
    id = current_user.id
    profile = Profile.objects.get(user=id)

    return redirect('profile', profile.id)


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
            'cities': cities,
            'profile': profile,
        }
        return render(request, 'city/city.html', context)

# __________________________________________________________
# ___________________     POSTS     ________________________
# __________________________________________________________

# ________________     Post Detail    _____________________
@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(id=post.profile_id)
    user = request.user
    current_profile = Profile.objects.get(user_id=user.id)
    # POST METHOD
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post_id = post_id
            new_comment.profile_id = current_profile.id
            new_comment.save()
            return redirect('post_detail', post_id)
    # GET METHOD
    else:
        form = CommentForm()
        context = {
            'post': post, 
            'profile': profile,
            'current_profile': current_profile,
            'form': form
        }
        return render(request, 'post_detail.html', context)

# _________________     Post EDIT   _______________________
@login_required
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    # POST METHOD
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('city_index', post.city_id)
    # GET METHOD
    else:
        form = PostForm(instance = post)
        return render(request, 'post_edit.html', {'post': post, 'form': form})

# _______________      Post DELETE   ______________________
@login_required
def post_delete(request, post_id):
    post = Post.objects.get(id = post_id)
    city_id = post.city_id
    Post.objects.get(id=post_id).delete()
    return redirect('city_index', city_id)

# __________________________________________________________
# ___________________     COMMENTS     _____________________
# __________________________________________________________

@login_required
def comment_edit(request, comment_id):
    the_comment = Comment.objects.get(id=comment_id)
    post = Post.objects.get(id=the_comment.post_id)
    profile = Profile.objects.get(id=post.profile_id)
    user = request.user
    current_profile = Profile.objects.get(user_id=user.id)
    # POST METHOD
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=the_comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post.id)
    # GET METHOD
    else:
        form = CommentForm(instance=the_comment)
        context = {
            'the_comment':the_comment,
            'post': post,
            'profile':profile,
            'current_profile':current_profile,
            'form':form,
        }
        return render(request, 'comment_edit.html', context)

def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    post = Post.objects.get(id=comment.post_id)
    comment.delete()
    return redirect('post_detail', post.id)