from django.contrib import admin
from .models import Content, History, Favorite

class ContentAdmin(admin.ModelAdmin):
    list_display = ("user", "title")
    list_display_links = ("user", "title")

admin.site.register(Content, ContentAdmin)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "typing_time")
    list_display_links = ("user",)

admin.site.register(History, HistoryAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "title",)
    list_display_links = ("user",)

admin.site.register(Favorite, FavoriteAdmin)