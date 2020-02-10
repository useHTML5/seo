# coding: utf-8
from __future__ import unicode_literals
# from urllib.parse import urlparse
# from django import http
# from django.conf import settings
# from django.contrib.redirects.models import Redirect
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.redirects.middleware import RedirectFallbackMiddleware
# from cms.utils.compat.dj import MiddlewareMixin
# from django.template.loader import render_to_string
# from django.template import engines
from django.shortcuts import redirect


class DisableCsrfCheck:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response


class RedirectToNonWww:
    """
    Иногда у нас не очень удобно делать редиректы с www сайтов в nginx
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        host = request.META.get('HTTP_HOST')

        if host and host.startswith('www.'):
            non_www = host.replace('www.', '')
            scheme = 'https' if request.is_secure() else 'http'
            return redirect('{}://{}{}'.format(scheme, non_www, request.get_full_path()))

        return response


# TODO надо бы проверять что у нас редиректы загружены вначале
# class CustomRedirectFallbackMiddleware(RedirectFallbackMiddleware):
#     response_gone_class = http.HttpResponseGone
#     response_redirect_class = http.HttpResponsePermanentRedirect
#
#     def process_response(self, request, response):
#         if response.status_code != 404:
#             return response
#
#         full_path = request.get_full_path()
#         """
#             Seperate query parameters and url if full absolute path contains
#             query parameters using python urlparse library
#         """
#         parsed_url = None
#         if "?" in full_path:
#             parsed_url = urlparse(full_path)
#             # Now full path contains no query parameters
#             full_path = parsed_url.path
#
#         current_site = get_current_site(request)
#
#         r = None
#         try:
#             r = Redirect.objects.get(site=current_site, old_path=full_path)
#         except Redirect.DoesNotExist:
#             pass
#         if r is None and settings.APPEND_SLASH and not request.path.endswith('/'):
#             try:
#                 if parsed_url is not None:
#                     r = Redirect.objects.get(
#                         site=current_site,
#                         old_path=full_path + '/',
#                     )
#                 else:
#                     r = Redirect.objects.get(
#                         site=current_site,
#                         old_path=request.get_full_path(force_append_slash=True),
#                     )
#             except Redirect.DoesNotExist:
#                 pass
#
#         if r is not None:
#             if r.new_path == '':
#                 return self.response_gone_class()
#
#             # Adding back the query parameters to redirecting path
#             if parsed_url is not None:
#                 new_path_with_query_params = r.new_path + "?" + parsed_url.query
#                 return self.response_redirect_class(new_path_with_query_params)
#
#             # Handles redirections for urls without query parameters
#             return self.response_redirect_class(r.new_path)
#
#         return response
