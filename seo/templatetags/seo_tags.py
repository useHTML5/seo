from django import template

register = template.Library()


@register.inclusion_tag('seo/data.html')
def seo_meta():
    try:
        from seo.meta.models import Meta
        meta = Meta.objects.filter(show=True).values_list('content', flat=True)
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
        from seo.counters.models import Counter
        counters = Counter.objects.filter(show=True).values_list('content', flat=True)
        return {
            'data': " ".join(counters)
        }
    except Exception as e:
        return {}


@register.inclusion_tag('seo/favicon.html')
def seo_favicon():
    try:
        from seo.favicon.models import Favicon
        favicon = Favicon.get_solo().favicon
        return {
            'data': favicon
        }
    except Exception as e:
        return {}
