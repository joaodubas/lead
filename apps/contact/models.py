#!/usr/bin/env python
# encoding: utf-8
from django.db import models


class Contact(models.Model):
    CHOICES = (
               ('SUG', 'Suggest one new feature'),
               ('BIL', 'Billing Informations'),
               ('BUG', 'Bug Report'),
               ('OUT', 'Other Report'),
               )

    category = models.CharField(choices=CHOICES, max_length=3, db_index=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
