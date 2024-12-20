from django import template

register = template.Library()

@register.filter
def hashtags(value):
    tags: list = value.replace(" ", "").split(",")
    tags_string = ""
    for i in tags:
        tags_string += "#" + i
        if i != tags[-1]:
            tags_string += " "
    return tags_string