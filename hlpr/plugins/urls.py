"""
Plugins URL Configuration
"""

from django.conf.urls import url
from .views import PluginListView, PluginDetailView, PluginLastUpdatedView, PluginStatsView

urlpatterns = [
    url(r'^$', PluginListView.as_view()),
    url(r'^last_updated/$', PluginLastUpdatedView.as_view()),
    url(r'^stats/$', PluginStatsView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/$', PluginDetailView.as_view())
]
