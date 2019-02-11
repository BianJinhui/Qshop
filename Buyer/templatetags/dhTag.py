from django import template
from . import dhpatterners
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def up(value):
    value = value.split("/")
    value = list(filter(None, value))
    content = ""
    for index,v in enumerate(value):
        if v in dhpatterners.keys():
            href = "/".join(value[:index+1])
            name = dhpatterners[v]
            content += '<a href="/%s">%s</a>&nbsp&nbsp>>>&nbsp&nbsp'%(href,name)
    return mark_safe(content.rstrip(">>>&nbsp&nbsp"))