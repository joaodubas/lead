#!/usr/bin/python
#encoding: utf-8
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    "first page without login"
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
    return render(request, 'home.html', {'form': form})
