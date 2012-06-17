#!/usr/bin/python
#encoding: utf-8
from models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
