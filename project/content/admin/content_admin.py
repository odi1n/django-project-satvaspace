from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin

from ..models import Content


class ContentInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Content
    extra = 0
