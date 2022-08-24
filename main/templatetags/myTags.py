from django import template
register = template.Library()

@register.filter
def getValue(value):
    if value == None:
        return ""
    else:
        return value