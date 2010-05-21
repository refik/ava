from django.template import Library

register = Library()

@register.filter
def get_range( value ):
	return range(1,value+1,1)
