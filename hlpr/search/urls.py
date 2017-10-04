from django.conf.urls import url
from .views import PluginSearchView

urlpatterns = [
    url(r'^$', PluginSearchView.as_view())
]
