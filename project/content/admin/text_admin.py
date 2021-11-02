from django.contrib import admin

from ..models import Text


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'page',
                    'text',
                    'counter']
    search_fields = ['title']


class TextStackedInline(admin.StackedInline):
    model = Text
    classes = ['collapse']
    extra = 1
