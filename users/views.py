from email import message
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginFrom, UserRegistrationForm, ProfileForm


def login(request):
    
    if request.method == 'POST':
        form = UserLoginFrom(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, "Вы вошли в аккаунт!")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginFrom()

    context = {
        'title': 'Home - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
                form.save()
                user = form.instance
                auth.login(request, user)
                messages.success(request, "Вы успешно зарегистрироавлись!")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()


    context = {
        'title': 'Home - Регистрация',
        'form': form,
    }
    
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
                form.save()
                messages.success(request, "Профиль обновлен!")
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    context = {
        'title': 'Home - Кабинет',
        'form': form,
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Вы вышли с аккаунта!")
    return redirect(reverse("main:index"))
