#!/usr/bin/python
#encoding: utf-8
from apps.contact.forms import ContactForm
from django.shortcuts import render


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'contact.html', {'form': form})
