from datetime import date
from django import template
register = template.Library()

@register.filter
def getValue(value):
    if value == None:
        return ""
    else:
        return value

@register.filter
def getEdad(fechaNacimiento):
    if fechaNacimiento:
        today = date.today() 
        edad = today.year - fechaNacimiento.year - ((today.month, today.day) < (fechaNacimiento.month, fechaNacimiento.day))
        return edad + " años"
    else:
        return ""