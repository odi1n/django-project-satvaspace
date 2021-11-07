import pytest
import json
from rest_framework.test import APIClient

from content.factory.audio_factories import AudioFactories
from content.factory.content_factories import ContentFactories
from content.factory.text_factories import TextFactories
from content.factory.video_factories import VideoFactories
from decision.factory.page_factories import PageFactories
from decision.models import Page

base_url = "/api/pages/"
api = APIClient()

@pytest.mark.django_db
class TestList:
    def test_list_pages_return_200(self):
        response = api.get(base_url, as_response=True)
        assert response.status_code == 200

    def test_pages_list_pagination(self):
        response = api.get(base_url)
        count_pages = Page.objects.all().count()
        assert response.data["count"] == count_pages
        assert response.data["next"] is not None

    def test_pages_list_results(self):
        response = api.get(base_url)
        page = Page.objects.all().first()
        result = response.data["results"][0]
        assert result["id"] == page.id
        assert result["title"] == page.title
        assert f"{base_url}{page.id}/" in result["absolute_url"]
