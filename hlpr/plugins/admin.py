from django.contrib import admin
from .models import Plugin, Version, File

admin.site.register(Plugin)
admin.site.register(Version)
admin.site.register(File)
