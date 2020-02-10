# coding: utf-8
from __future__ import unicode_literals
from django.urls import re_path
from django.http import HttpResponse
from django.db.utils import ProgrammingError
import re


class FileUrls(object):

    def gen_http(self, content, name):
        def response_function(*args, **kwargs):
            response = HttpResponse(content, content_type='text/plain')
            response['Content-Disposition'] = 'filename="{}"'.format(name)
            return response

        return response_function

    def get_urls(self):
        from . import models
        urls = []
        try:
            for f in models.ConfirmFile.objects.all():
                urls.append(re_path(r'^{}$'.format(re.escape(f.url)), self.gen_http(f.content, f.url)))
        except ProgrammingError as e:
            # Еще не была создана модель, потому идут проблемы
            pass
        return urls

    @property
    def urls(self):
        return self.get_urls(), 'seo_files'


seo = FileUrls()
