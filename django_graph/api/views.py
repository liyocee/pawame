from rest_framework import permissions
from rest_framework import viewsets

from .models import RandomNumber
from .serializers import RandomNumberSerializer

class RandomNumberViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RandomNumberSerializer
    queryset = RandomNumber.objects.all()
