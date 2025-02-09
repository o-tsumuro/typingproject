from django.contrib import admin
from .models import History, Favorite

class HistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "typing_time")
    list_display_links = ("user",)

admin.site.register(History, HistoryAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "title",)
    list_display_links = ("user",)

admin.site.register(Favorite, FavoriteAdmin)