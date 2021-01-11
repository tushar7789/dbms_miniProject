from django import template
from store.models.shipper import Shipping_Route

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹"+str(number)

@register.filter(name='multiply')
def multiply(n1, n2):
    return n1*n2



