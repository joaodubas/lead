#!/usr/bin/python
#encoding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.urlresolvers import reverse
from apps.contact.forms import ContactForm


def home(request):
    "first page without login"
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
    return render(request, 'home.html', {'form': form})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'contact.html', {'form': form})


def signin(request):
    form = AuthenticationForm(request or None)
    if form.is_valid():
        login(request, form.get_user())
    return render(request, 'signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect(reverse('home'))
