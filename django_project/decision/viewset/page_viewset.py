from rest_framework import viewsets, authentication, permissions
from rest_framework.response import Response

from ..models import Page
from ..serializer import PageSerializer


class PageViewSet(viewsets.ViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # def list(self, request):
    #     return self.account_service.list(request.user)

    def retrieve(self, request, pk=0):
        page = Page.objects.filter(id=pk).first()
        if not page:
            return Response({"error": "not page"})
        serializer = PageSerializer(page)
        return Response(data=serializer.data)
