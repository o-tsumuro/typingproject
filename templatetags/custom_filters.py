from django import template

register = template.Library()

@register.filter
def format_duration(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}分{remaining_seconds}秒"