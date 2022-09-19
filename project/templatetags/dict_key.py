from collections import defaultdict

from django.template.defaultfilters import register


@register.filter(name='key')
def key(d: defaultdict, k):
    return d[k]
