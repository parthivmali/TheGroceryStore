from django import template

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return "₹ " + str(number) + "/-"

@register.filter(name='number')
def number(number):
    return "+91  " + str(number)