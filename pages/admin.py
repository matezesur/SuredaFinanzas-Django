from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'subtitulo', 'categoria')
    list_filter = ('categoria', 'fecha_publicacion')
