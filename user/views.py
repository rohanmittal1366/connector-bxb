from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required # for give permision according to the user and admin


# Create your views here.

#  for register user
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form' : form,
    } 
    return render(request, 'user/register.html', context)

@login_required(login_url='user-login')
def profile(request):
    return render(request, 'user/profile.html')

# for updating user/profile

@login_required(login_url='user-login')
def profile_update(request):
    # user_form to update User table and profile_form to update Profile table in database
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # what instance do is it already load data so that we can edit it  
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    # because we want to update more than one form so we pass context as one parameter
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/profile_update.html', context)
