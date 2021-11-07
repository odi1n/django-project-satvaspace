import pytest
import json
from rest_framework.test import APIClient

from content.factory.audio_factories import AudioFactories
from content.factory.content_factories import ContentFactories
from content.factory.text_factories import TextFactories
from content.factory.video_factories import VideoFactories
from content.models import Content
from decision.factory.page_factories import PageFactories
from decision.models import Page

base_url = "/api/pages/"
max_counter = 50
api = APIClient()


@pytest.fixture
def content_audio():
    return AudioFactories()


@pytest.fixture
def content_text():
    return TextFactories()


@pytest.fixture
def content_video():
    return VideoFactories()


@pytest.fixture
def page(content_text, content_audio, content_video):
    page = PageFactories()
    Content.objects.create(page=page, content_text=content_text)
    Content.objects.create(page=page, content_audio=content_audio)
    Content.objects.create(page=page, content_video=content_video)
    return page


@pytest.mark.django_db
class TestDetails:
    def test_pages_detail_return_200(self, page):
        response = api.get(f'{base_url}1/', as_response=True)
        assert response.status_code == 200

    def test_pages_detail_return_404(self):
        response = api.get(f'{base_url}99999/', as_response=True)
        assert response.status_code == 404

    def test_pages_detail_data(self, page):
        response = api.get(f'{base_url}{page.id}/', as_response=True)

        assert response.data['id'] == page.id
        assert response.data['title'] == page.title

    def test_pages_detail_text(self, page, content_text):
        response = api.get(f'{base_url}{page.id}/', as_response=True)

        text = response.data["contents"][0]["content_text"]
        assert text['id'] == content_text.id
        assert text['title'] == content_text.title
        assert text['text'] == content_text.text

    def test_pages_detail_audio(self, page, content_audio):
        response = api.get(f'{base_url}{page.id}/', as_response=True)

        text = response.data["contents"][1]["content_audio"]
        assert text['id'] == content_audio.id
        assert text['title'] == content_audio.title
        assert text['link'] == content_audio.link
        assert text['bitrate'] == content_audio.bitrate
        assert text['bit_in_second'] == content_audio.bit_in_second

    def test_pages_detail_video(self, page, content_video):
        response = api.get(f'{base_url}{page.id}/', as_response=True)

        text = response.data["contents"][2]["content_video"]
        assert text['id'] == content_video.id
        assert text['title'] == content_video.title
        assert text['link_subtitles'] == content_video.link_subtitles
