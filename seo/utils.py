# coding: utf-8
from __future__ import unicode_literals
from django.core import management
from django.core.cache import cache
from django.db.models.signals import post_save
import os
from django.conf import settings
from cms.models.pagemodel import Page


def reload_uwsgi(sender, **kwargs):
    reload_path = os.path.join(settings.BASE_DIR, '..', 'reload')
    os.system("touch {}".format(reload_path))


def reload_uwsgi_after_save(model):
    post_save.connect(reload_uwsgi, sender=model)


def delete_cache(sender, **kwargs):
    cache.clear()


def delete_cache_after_save(model):
    post_save.connect(delete_cache, sender=model)


delete_cache_after_save(Page)
