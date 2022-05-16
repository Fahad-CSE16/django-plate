from django import template

register = template.Library()


@register.simple_tag()
def calculation(value, arg, operator):
    try:
        if operator == '*':
            return value * arg
        elif operator == '-':
            return value - arg
        elif operator == '+':
            return value + arg
    except:
        return 0


@register.filter
def get_item(data, key):
    return data.get(key)


@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def field_name_to_label(value):
    value = value.replace('_', ' ')
    return value.title()