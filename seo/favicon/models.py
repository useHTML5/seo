# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from filer.fields.file import FilerFileField
from seo.utils import delete_cache_after_save, reload_uwsgi_after_save
from solo.models import SingletonModel


class Favicon(SingletonModel):
    favicon = FilerFileField(related_name='favicon', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Favicon'
        verbose_name_plural = 'Faviconка'


delete_cache_after_save(Favicon)
