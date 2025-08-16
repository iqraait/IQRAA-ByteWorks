from django import template

register = template.Library()

@register.filter
def get_field(form, field_name):
    """
    Template filter to get a form field by name dynamically.
    Usage: {{ form|get_field:"field_name" }}
    """
    try:
        return form[field_name]
    except KeyError:
        return None
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)