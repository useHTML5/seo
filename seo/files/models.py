# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from seo.utils import delete_cache_after_save, delete_cache, reload_uwsgi_after_save


class ConfirmFile(models.Model):
    url = models.CharField(max_length=255, verbose_name='Путь')
    name = models.CharField(max_length=255, verbose_name='Описание', blank=True, null=True)
    show = models.BooleanField('Показывать', default=True)
    content = models.TextField(verbose_name='Содержимое файла', blank=True)

    def __unicode__(self):
        return self.url

    class Meta:
        verbose_name = 'Файл подтвержения'
        verbose_name_plural = 'Файлы подтверждения'


reload_uwsgi_after_save(ConfirmFile)
