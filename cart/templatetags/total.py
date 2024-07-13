from django import template


register = template.Library()



@register.filter()
def total(price,quantity):
    return price*quantity
