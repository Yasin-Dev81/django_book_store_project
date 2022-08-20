from django import template


register = template.Library()


# STATUS_CHOICES
@register.filter
def STATUS_CHOICES_DICT(input_tuple: tuple):
    return dict((x, y) for x, y in input_tuple)


# book_status
@register.filter
def book_status(input_tuple: tuple, value: str):
    return STATUS_CHOICES_DICT(input_tuple).get(value)
