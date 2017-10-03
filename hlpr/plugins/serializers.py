from rest_framework import serializers, fields
from hlpr.user.serializers import UserListSerializer
from .choices import CategoryChoices
from .models import Plugin, Version


class VersionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('version', 'archive',)


class VersionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('version', 'archive',)


class PluginListSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)

    class Meta:
        model = Plugin
        fields = ('name', 'author', 'slug', 'last_updated', 'summary', 'game', 'mod', 'category')


class PluginDetailSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)
    collaborators = UserListSerializer(read_only=True, many=True)
    versions = VersionListSerializer(read_only=True, many=True)

    class Meta:
        model = Plugin
        fields = ('name', 'slug', 'description', 'summary', 'author', 'collaborators', 'created',
                  'last_updated', 'category', 'game', 'versions')
