from django.conf.urls import url

from federation.hostmeta.django import rfc3033_webfinger_view
from federation.hostmeta.django.generators import nodeinfo2_view

urlpatterns = [
    url(r'^.well-known/webfinger$', rfc3033_webfinger_view, name="rfc3033-webfinger"),
    url(r'^.well-known/x-nodeinfo2$', nodeinfo2_view, name="nodeinfo2"),
]
