from django import template
register = template.Library()
@register.filter(name="max_value")

def max_value(value):
    value_list = []
    value_list.append(value)
    return max(value_list)