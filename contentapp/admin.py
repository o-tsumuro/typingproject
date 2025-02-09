from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "is_public")
    list_display_links = ("user", "title")

admin.site.register(Content, ContentAdmin)
