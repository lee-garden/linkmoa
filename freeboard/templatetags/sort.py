from django.template import Library
from .. import models

register = Library()

@register.inclusion_tag('freeboardSearch.html')
def sort_order_by_views(queryset):
    searched_posts = queryset.order_by('-views')
    print(searched_posts)
    return {'searched_posts' : searched_posts}