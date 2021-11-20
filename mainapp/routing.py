from django.urls import re_path, path
from . import consumers

ws_urlpatterns = [
    re_path(r'ws/stock/',
            consumers.StockConsumer.as_asgi()),
]
