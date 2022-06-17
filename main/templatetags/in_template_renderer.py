from django import template
from django.template import Template
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def in_template_renderer(context, template_string):
   template = Template(template_string)
   return mark_safe(template.render(context))