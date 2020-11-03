from django import template
from django.core.cache import cache
register = template.Library()


@register.inclusion_tag('seo/data.html')
def seo_meta():
    try:
        meta = cache.get('seo_meta')
        if meta is None:
            from seo.meta.models import Meta
            meta = Meta.objects.filter(show=True).values_list('content', flat=True)
            cache.set('seo_meta', meta)
        return {
            'data': " ".join(meta)
        }
    except Exception as e:
        return {}


@register.simple_tag()
def seo_param(param, name='', value=False):
    from seo.params.models import Param
    try:
        p = Param.objects.get(name=param)
    except Param.DoesNotExist:
        p = Param(name=param, title=name or param, default='НЕ_ЗАДАН_{}'.format(param))
        p.save()
    if value:
        return p.default
    else:
        return p


@register.inclusion_tag('seo/data.html')
def seo_counters():
    try:
        counters = cache.get('seo_counters')
        if counters is None:
            from seo.counters.models import Counter
            counters = Counter.objects.filter(show=True).values_list('content', flat=True)
            cache.set('seo_counters', counters)
        return {
            'data': " ".join(counters)
        }
    except Exception as e:
        return {}


@register.inclusion_tag('seo/favicon.html')
def seo_favicon():
    try:
        favicon = cache.get('seo_favicon')
        if favicon is None:
            from seo.favicon.models import Favicon
            favicon = Favicon.get_solo().favicon
            cache.set('seo_favicon', favicon)
        return {
            'data': favicon
        }
    except Exception as e:
        return {}
