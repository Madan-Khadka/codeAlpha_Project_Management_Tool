import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from projects.routing import websocket_urlpatterns


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "project_management.settings"
)


# Standard Django ASGI application
django_asgi_app = get_asgi_application()


# ---------------------------------------------------------
# ASGI APPLICATION
# ---------------------------------------------------------

application = ProtocolTypeRouter({

    # Normal HTTP requests
    "http": django_asgi_app,

    # WebSocket requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})