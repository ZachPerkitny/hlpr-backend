from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from hlpr.user.models import User
from .models import Plugin
from .serializers import PluginListSerializer, PluginDetailSerializer


class PluginListFilter(filters.FilterSet):
    """
    FilterSet for the Plugin List View
    """

    author = filters.CharFilter(name='author__username', lookup_expr='iexact')

    class Meta:
        model = Plugin
        fields = ['author', 'mod', 'game', 'name']


class PluginListView(ListCreateAPIView):
    """
    Gets a list of plugins by filtering against
    the author, name or mod or creates a new plugin.
    """

    queryset = Plugin.objects.all()
    serializer_class = PluginListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PluginListFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PluginDetailView(RetrieveAPIView):
    """
    Gets a plugin by filtering against its slug
    """

    queryset = Plugin.objects.all()
    serializer_class = PluginDetailSerializer
    lookup_field = 'slug'


class PluginLastUpdatedView(APIView):
    """
    Returns the 10 latest plugins.
    """

    def get(self, request, format=None):
        queryset = Plugin.objects.all().order_by('last_updated')[:10]
        serializer = PluginListSerializer(queryset, many=True)
        return Response(serializer.data)


class PluginStatsView(APIView):
    """
    Returns various stats about the Plugin models:
    Plugin Count, # of Authors
    """

    def get(self, request, format=None):
        authors_count = User.objects.filter(plugin_author__isnull=False).distinct().count()
        plugin_count = Plugin.objects.count()
        content = {
            'authors_count': authors_count,
            'plugin_count': plugin_count
        }
        return Response(content)
