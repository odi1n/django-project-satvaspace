from rest_framework import serializers

from ..models import Page
from content.serializer import AudioSerializer, TextSerializer, VideoSerializer


class PageSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    audio = AudioSerializer(many=True, read_only=True)
    text = TextSerializer(many=True, read_only=True)
    video = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id',
                  'title',
                  'audio',
                  'text',
                  'video']
