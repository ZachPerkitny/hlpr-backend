"""
Plugins URL Configuration
"""

from django.conf.urls import url
from .views import (PluginListView, PluginDetailView, PluginExistsView, PluginLastUpdatedView,
                    PluginStatsView, VersionListView, VersionDetailView, VersionExistsView)

urlpatterns = [
    url(r'^$', PluginListView.as_view()),
    url(r'^last_updated/$', PluginLastUpdatedView.as_view()),
    url(r'^stats/$', PluginStatsView.as_view()),
    url(r'^exists/(?P<slug>[-_\w]+)/$', PluginExistsView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/$', PluginDetailView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/versions/$', VersionListView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/versions/(?P<version>(?:\d\.?){1,4})/$',
        VersionDetailView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/versions/exists/(?P<version>(?:\d\.?){1,4})/$',
        VersionExistsView.as_view())
]
