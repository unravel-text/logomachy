from django import template
from django.conf import settings
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def app_settings(setting_name, default_value=None):
    value = getattr(settings, setting_name, default_value)
    return value


def is_active(context, value):
    if not value:
        return False
    request = context.get('request')
    if request:
        url_name = request.resolver_match.url_name
        return url_name == value


@register.simple_tag(takes_context=True)
def sr_only(context, value):
    if is_active(context, value):
        return format_html(' <span class="sr-only">(current)</span>')
    else:
        return ''


@register.simple_tag(takes_context=True)
def nav_item_active(context, value):
    if is_active(context, value):
        return 'active'
    else:
        return ''
