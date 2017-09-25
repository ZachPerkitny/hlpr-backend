"""
HLPR URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^plugins/', include('hlpr.plugins.urls')),
    url(r'^user/', include('hlpr.user.urls'))
]
