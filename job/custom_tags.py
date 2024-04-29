from django import template

register = template.Library()

@register.filter
def add_dot_to_each_line(value):
    lines = value.splitlines()
    dotted_lines = ["• " + line.strip() for line in lines if line.strip()]
    return "\n".join(dotted_lines)