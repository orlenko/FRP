from haystack import indexes

class MemberIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    agency = indexes.CharField(model_attr='agency')
    site_updated = indexes.DateTimeField(model_attr='site_updated')

    def get_model(self):
        from memdir.models import Member # or else a circ import
        return Member

    def index_queryset(self):
        """ Used when entire index is updated """
        return self.get_model().objects.filter(is_frp_member=True)
