from django import template

register = template.Library()

@register.filter
def ensure_protocol(value):
    if value.startswith('http://') or value.startswith('https://'):
        return value
    return 'http://' + value
