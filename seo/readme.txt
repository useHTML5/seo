

from site_app_seo.views import seo

urlpatterns = [
    url(r'^', include(seo.urls)),
]

{% load site_app_seo_tags %}

<head>
{% seo_meta %}
{% seo_favicon %}

<body>
{% seo_counters %}

{% seo_counters %}

'seo.middleware.CustomRedirectFallbackMiddleware', #вместо обычного redirect mv, ибо тот параметры не учитывает