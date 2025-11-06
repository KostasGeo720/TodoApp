from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
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