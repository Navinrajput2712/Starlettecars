from django import template
from datetime import date

register = template.Library()

@register.filter
def add(value, arg):
    try:
        return float(value) + float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

    
@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def days_until(rental_date):
    """Calculate days until rental date"""
    try:
        today = date.today()
        if hasattr(rental_date, 'date'):
            rental_date = rental_date.date()
        delta = rental_date - today
        return delta.days
    except (ValueError, TypeError, AttributeError):
        return 0
    

