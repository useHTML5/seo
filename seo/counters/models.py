# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from seo.utils import delete_cache_after_save, delete_cache, reload_uwsgi_after_save


class Counter(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    show = models.BooleanField('Работает', default=False)
    content = models.TextField(verbose_name='Код счетчика', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчики'


delete_cache_after_save(Counter)
