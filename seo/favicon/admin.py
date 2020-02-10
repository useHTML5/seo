# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from . import models
from solo.admin import SingletonModelAdmin


@admin.register(models.Favicon)
class FaviconAdmin(SingletonModelAdmin):
    pass
