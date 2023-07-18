from django.shortcuts import render, redirect
from .forms import *


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    user = request.user
    data = {'user': user}
    return render(request, template_name='users/profile.html', context=data)


def update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect(to='home')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'users/update_profile.html', {'user_form': user_form})
