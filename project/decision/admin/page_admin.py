from django.contrib import admin

from content.models import Content
from ..models import Page
from content.admin import ContentInline


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ContentInline]
    search_fields = [
        "title__istartswith",
        *[f"contents__{x.name}__title__istartswith" for x in Content.get_content_fields()],
    ]
