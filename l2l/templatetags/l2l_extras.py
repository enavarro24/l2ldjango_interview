from django import template

register = template.Library()


@register.simple_tag
def my_custom_tag():
    return "Custom tag"
