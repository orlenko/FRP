import haystack.indexes
from memdir.models import Location


class LocationIndex(haystack.indexes.RealTimeSearchIndex, haystack.indexes.Indexable):
    text = haystack.indexes.CharField(document=True, use_template=True)
    frp_program_name = haystack.indexes.CharField(model_attr='frp_program_name')
    region = haystack.indexes.CharField(model_attr='region')
    community = haystack.indexes.CharField(model_attr='community')

    def get_model(self):
        return Location

    def index_queryset(self):
        """ Used when entire index is updated """
        return self.get_model().objects.all()

