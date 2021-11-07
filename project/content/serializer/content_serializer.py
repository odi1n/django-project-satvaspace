from rest_framework import serializers

from ..models import Content
from . import TextSerializer, AudioSerializer, VideoSerializer


class ContentSerializer(serializers.ModelSerializer):
    content_audio = AudioSerializer()
    content_text = TextSerializer()
    content_video = VideoSerializer()

    class Meta:
        model = Content
        fields = ['id',
                  'content_audio',
                  'content_text',
                  'content_video']
