import json

from django import template
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html
from django_ckeditor_5.widgets import CKEditor5Widget


register = template.Library()


@register.simple_tag()
def ckeditor_config(config_name):
    widget = CKEditor5Widget(config_name=config_name)

    s = json.dumps(widget.config)
    print(s)
    return s
