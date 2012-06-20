#!/usr/bin/python
#encoding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.urlresolvers import reverse


def signin(request):
    form = AuthenticationForm(request or None)
    if form.is_valid():
        login(request, form.get_user())
    return render(request, 'signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect(reverse('home'))
