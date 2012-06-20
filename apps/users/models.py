#!/usr/bin/env python
# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from apps.core.models import DefaultFields
from django.conf import settings

import hashlib


class Follow(DefaultFields):
    owner = models.ForeignKey(User, related_name='followers')
    friend = models.ForeignKey(User, related_name='following')

    def __unicode__(self):
        return self.owner


class UserProfile(DefaultFields):
    "Extending User with DefaultFields"
    user = models.OneToOneField(User)
    initials = models.CharField(max_length=2, db_index=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
    token = models.CharField(max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return '/u/%s/' % self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    "Signal to auto create user"
    if created:
        django_token = str(settings.SECRET_KEY + instance.email)
        instance.token = hashlib.md5(django_token).hexdigest()
        django_initials = str(instance.first_name[:1] + instance.last_name[:1]).upper()
        instance.initials = django_initials
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
