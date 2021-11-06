from django.urls import reverse
from rest_framework import serializers

from content.serializer.content_serializer import ContentSerializer
from ..models import Page


class PagesSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    def get_absolute_url(self, obj):
        url = reverse("pages-detail", args=(obj.id,))
        request = self.context.get("request")
        absolute_url = request.build_absolute_uri(url) if request else url
        return absolute_url

    class Meta:
        model = Page
        fields = ["id", "title", "absolute_url"]


class PageSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    @classmethod
    def many_init(cls, *args, **kwargs):
        return PagesSerializer(*args, **kwargs, many=True)

    class Meta:
        model = Page
        fields = ['id',
                  'title',
                  'contents']
