from rest_framework import viewsets

from ..models import Page
from ..serializer import PageSerializer
from ..tasks import increasing_counter_page_task


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        increasing_counter_page_task.delay(data.id)
        return super().retrieve(request, *args, **kwargs)
