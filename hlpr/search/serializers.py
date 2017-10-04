from drf_haystack.serializers import HaystackSerializerMixin
from hlpr.plugins.serializers import PluginListSerializer


class PluginSearchSerializer(HaystackSerializerMixin, PluginListSerializer):

    class Meta(PluginListSerializer.Meta):
        search_fields = ('text', 'name', 'game')
        field_aliases = {}
        exclude = tuple()
