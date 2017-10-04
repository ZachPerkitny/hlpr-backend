from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView
from .serializers import PluginSearchSerializer


class PluginSearchView(ListModelMixin, HaystackGenericAPIView):
    """
    Search View
    """

    serializer_class = PluginSearchSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

