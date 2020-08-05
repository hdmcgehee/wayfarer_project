from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Define the home view
def home(request):
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
        print('elif block hit')
        return redirect('home')
    else:
      return redirect('home')
  else:
    return render(request, 'home.html', context)


def city_detail(request):
  return render(request, 'city/detail.html')