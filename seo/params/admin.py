# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from . import models
from seo.utils import delete_cache_after_save
from cms.admin.placeholderadmin import FrontendEditableAdminMixin

@admin.register(models.Param)
class ParamAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'name', 'default']


delete_cache_after_save(models.Param)
