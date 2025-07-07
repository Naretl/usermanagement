from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import RegistrationForm, ProfileForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)

            # ✅ Simulated email verification
            send_mail(
                subject='Verify Your Email',
                message='Welcome! Your account is created. This is a simulated verification.',
                from_email='no-reply@example.com',
                recipient_list=[user.email],
                fail_silently=True
            )

            messages.success(request, "Registration successful! A verification email (mock) was sent.")
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    profile = request.user.userprofile
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})



