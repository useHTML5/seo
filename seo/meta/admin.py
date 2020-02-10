# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from . import models


@admin.register(models.Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = 'name', 'show', 'content'
