#!/usr/bin/env python
# encoding: utf-8
import re
from django.db import models
from apps.core.models import DefaultFields
from apps.tag.models import Tag
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings


class State(models.Model):
    STATUS_CHOICE = (
                     ('STA', 'Start'),
                     ('END', 'Finished'),
                     ('RJC', 'Rejected'),
                     ('DEL', 'Delivery'),
                     )
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, default='STA', max_length=3, db_index=True)

    def __unicode__(self):
        return self.updated_at, self.get_status_display()


class Ticket(DefaultFields):
    CHOICE_CATEGORY = (
                   ('BUG', 'Bug'),
                   ('FEA', 'Feature'),
                   ('CHO', 'Chore'),
                   )

    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    points = models.IntegerField(default=0)
    states = models.ManyToManyField(State)
    members = models.ManyToManyField(User)
    category = models.CharField(max_length=3, default='ENC', choices=CHOICE_CATEGORY)

    def add_tag(self, values):
        tags = list(set(re.split(',| |-|/|\"|\'|\\n', values)))  # split value
        if '' in tags:
            tags.remove('')
        created = []
        for tag in tags:
            created.append(self.tags.get_or_create(value=slugify(tag)))
        return created

    def __unicode__(self):
        return self.title


class CheckList(DefaultFields):
    ticket = models.ForeignKey(Ticket, related_name='ticket_set')
    owner = models.ForeignKey(User, related_name='checklist_owner_set')
    title = models.CharField(max_length=150)

    def __unicode__(self):
        return self.title


class Task(DefaultFields):
    title = models.CharField(max_length=150)
    checklist = models.ForeignKey(CheckList, related_name='task_set')

    def __unicode__(self):
        return self.title


def get_img_storage_path(instance, filename):
    return '%s/tickets/%s/%Y/%m/%d/' % (settings.MEDIA_ROOT, instance.ticket.pk)


class TicketFiles(DefaultFields):
    ticket = models.ForeignKey(Ticket, related_name='files_set')
    upload = models.FileField(upload_to=get_img_storage_path)

    def __unicode__(self):
        return self.upload
