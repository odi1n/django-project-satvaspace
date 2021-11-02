from django.contrib import admin

from ..models import Audio


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'page',
                    'bitrate',
                    'bit_in_second',
                    'counter']
    search_fields = ['title']


class AudioStackedInline(admin.StackedInline):
    model = Audio
    classes = ['collapse']
    extra = 1
