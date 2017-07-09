from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from api.bindings import RandomNumberBinding

class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'random_number': RandomNumberBinding.consumer
    }

channel_routing = [
    route_class(APIDemultiplexer)
]
