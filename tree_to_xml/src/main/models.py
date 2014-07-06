__author__ = 'alex'
# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Structure(MPTTModel):
    TYPE_CHOICE = (
        ('d', 'Directory'),
        ('f', 'File'),
    )
    name = models.CharField(max_length=50)
    type = models.CharField(u"Type", max_length=1, choices=TYPE_CHOICE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    created = models.IntegerField(max_length=11, default=0)

    class MPTTMeta:
        order_insertion_by = ['name']