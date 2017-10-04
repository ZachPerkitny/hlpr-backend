from haystack import indexes
from hlpr.plugins.models import Plugin


class PluginIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    name = indexes.CharField(model_attr='name')
    game = indexes.CharField(model_attr='game')

    def get_model(self):
        return Plugin

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
