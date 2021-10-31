from django.contrib import admin

from ..models import Page
from content.admin import TextStackedInline, AudioStackedInline, VideoStackedInline


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'counter']
    inlines = [TextStackedInline, AudioStackedInline, VideoStackedInline]
