from django.utils import timezone

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

class CachedEndpoint(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):

        page = {
            "title": "This should be cached",
            "served_at": timezone.now()
        }
        return Response(page)


class NonCachedEndpoint(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):

        page = {
            "title": "This should never be cached",
            "served_at": timezone.now()
        }
        return Response(page)
