from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from friends import routing as friends_routing
from notifications import routing as notifications_routing
from chat import routing as chat_routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            friends_routing.websocket_urlpatterns + notifications_routing.websocket_urlpatterns + chat_routing.websocket_urlpatterns
        )),
})
