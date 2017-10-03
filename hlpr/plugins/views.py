from rest_framework.generics import (ListCreateAPIView, RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from hlpr.user.models import User
from .models import Plugin, Version
from .permissions import IsOwnerOrReadOnly
from .serializers import (PluginListSerializer, PluginDetailSerializer, VersionListSerializer,
                          VersionDetailSerializer)


class PluginListView(ListCreateAPIView):
    """
    Gets a list of plugins by filtering against
    the author, name or mod or creates a new plugin.
    """

    serializer_class = PluginListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        Optionally filters plugin list by user id
        """
        queryset = Plugin.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            queryset = queryset.filter(author=user_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PluginDetailView(RetrieveUpdateDestroyAPIView):
    """
    Gets a plugin by filtering against its slug
    """

    queryset = Plugin.objects.all()
    serializer_class = PluginDetailSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = 'slug'


class PluginExistsView(APIView):
    """
    Checks if a plugin exists
    """

    def get(self, request, slug, **kwargs):
        try:
            Plugin.objects.get(slug=slug)
        except Plugin.DoesNotExist:
            return Response({'created': False})
        return Response({'created': True})


class PluginLastUpdatedView(APIView):
    """
    Returns the 10 latest plugins.
    """

    def get(self, request, format=None):
        queryset = Plugin.objects.all().order_by('-last_updated')[:10]
        serializer = PluginListSerializer(queryset, many=True)
        return Response(serializer.data)


class PluginStatsView(APIView):
    """
    Returns various stats about the Plugin models:
    Plugin Count, # of Authors
    """

    def get(self, request, format=None):
        authors_count = User.objects.filter(plugins__isnull=False).distinct().count()
        plugin_count = Plugin.objects.count()
        content = {
            'authors_count': authors_count,
            'plugin_count': plugin_count
        }
        return Response(content)


class VersionListView(ListCreateAPIView):
    """
    Gets a list of versions for a plugin.
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = VersionListSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Version.objects.filter(plugin__slug=slug)

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        serializer.save(plugin=Plugin.objects.get(slug=slug))


class VersionDetailView(RetrieveAPIView):
    """
    Gets a specific version and its files.
    """

    queryset = Version.objects.all()
    serializer_class = VersionDetailSerializer
    lookup_fields = ('slug', 'version',)

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(
            queryset,
            plugin__slug=self.kwargs['slug'],
            version=self.kwargs['version']
        )


class VersionExistsView(APIView):
    """
    Checks if a version exists
    """

    def get(self, request, slug, version, **kwargs):
        try:
            Version.objects.get(plugin__slug=slug, version=version)
        except Version.DoesNotExist:
            return Response({'created': False})
        return Response({'created': True})
