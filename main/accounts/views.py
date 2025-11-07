from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .forms import NewUserProfileForm

def new_profile(request):
    if request.method == 'POST':
        form = NewUserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Profile created successfully!')
            return redirect('new_profile')
        else:
            messages.error(request, 'Invalid Form Submission! Please correct the errors.')
    else:
        form = NewUserProfileForm()
    return render(request, 'accounts/new_profile.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})