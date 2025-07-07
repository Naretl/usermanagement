from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, ProfileForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    profile = request.user.userprofile
    return render(request, 'accounts/profile.html', {'profile': profile})

def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
