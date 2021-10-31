from rest_framework import serializers

from ..models import Page
from content.serializer import AudioSerializer, TextSerializer, VideoSerializer


class PagesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pages-detail')

    class Meta:
        model = Page
        fields = ['url']


class PageSerializer(serializers.ModelSerializer):
    audio = AudioSerializer(many=True)
    text = TextSerializer(many=True)
    video = VideoSerializer(many=True)

    class Meta:
        model = Page
        fields = ['id',
                  'title',
                  'audio',
                  'text',
                  'video']
