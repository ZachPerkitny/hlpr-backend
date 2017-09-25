from rest_framework import serializers
from hlpr.user.serializers import UserListSerializer
from .models import Plugin


class PluginListSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)

    class Meta:
        model = Plugin
        fields = ('name', 'author', 'slug', 'last_updated', 'description', 'game', 'mod')


class PluginDetailSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)
    collaborators = UserListSerializer(read_only=True, many=True)

    class Meta:
        model = Plugin
        fields = ('name', 'slug', 'description', 'author', 'collaborators', 'created',
                  'last_updated', 'category', 'game', 'mod')
