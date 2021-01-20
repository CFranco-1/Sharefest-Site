from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, EditProfileForm, ProfileForm
from .models import UserProfile
from datetime import datetime

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login.')
		return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user)
		#profile_form = ProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user_form = form.save()
			custom_form = profile_form.save()
			custom_form.user = user_form
			custom_form.save()
			messages.success(request, 'Profile details updated.')
			return redirect('profile')
	else:
		form = EditProfileForm(instance=request.user)
		#profile_form = ProfileForm(instance=request.user.userprofile)
		profile_form = ProfileForm()
		args = {}
		# args.update(csrf(request))
		args['form'] = form
		args['profile_form'] = profile_form
        
	return render(request, 'users/profile.html', args)