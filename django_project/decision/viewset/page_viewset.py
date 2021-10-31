from rest_framework import viewsets, authentication, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from ..models import Page
from ..serializer import PageSerializer, PagesSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PagesSerializer

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=0):
        page = Page.objects.filter(id=pk).first()
        if not page:
            return Response({"error": "not page"})
        serializer = PageSerializer(page)
        return Response(data=serializer.data)
