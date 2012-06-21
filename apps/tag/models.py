#!/usr/bin/env python
# encoding: utf-8
from django.db import models
from apps.core.models import DefaultFields


class Tag(DefaultFields):
    value = models.CharField(max_length=100)

    def __unicode__(self):
        return self.value
