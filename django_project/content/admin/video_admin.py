from django.contrib import admin

from ..models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'page',
                    'link',
                    'link_subtitles',
                    'counter']


class VideoStackedInline(admin.StackedInline):
    model = Video
