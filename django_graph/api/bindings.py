from channels_api.bindings import ResourceBinding

from .models import RandomNumber
from .serializers import RandomNumberSerializer

class RandomNumberBinding(ResourceBinding):

    model = RandomNumber
    stream = "random_number"
    serializer_class = RandomNumberSerializer
    queryset = RandomNumber.objects.all()
