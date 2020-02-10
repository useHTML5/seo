# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from cms.models import CMSPlugin


class Param(models.Model):
    title = models.CharField(verbose_name='Название для людей', max_length=255, blank=True, null=True)
    name = models.SlugField(verbose_name='Название в шаблоне', max_length=255,
                            help_text="писать латинскими без пробелов и без {{")
    default = models.TextField(verbose_name='Значение стандартное', blank=True, null=True)

    def __str__(self):
        return self.default

    class Meta:
        verbose_name = 'Параметр шаблона'
        verbose_name_plural = 'Параметры шаблона'
        unique_together = 'name',
