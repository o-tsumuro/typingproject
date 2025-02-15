from django.contrib import admin
from .models import Content, Category

class ContentAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "category", "is_public", "play_count",)
    list_display_links = ("user", "title")

admin.site.register(Content, ContentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Category, CategoryAdmin)