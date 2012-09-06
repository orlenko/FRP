from haystack import indexes

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    
    def get_model(self):
        from news.models import Post
        return Post

    def index_queryset(self):
        """ Used when entire index is updated """
        return self.get_model().objects.all()

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    start = indexes.DateTimeField(model_attr='start')
    end = indexes.DateTimeField(model_attr='end')
    description = indexes.CharField(model_attr='description')
    
    def get_model(self):
        from news.models import Event
        return Event

    def index_queryset(self):
        """ Used when entire index is updated """
        return self.get_model().objects.all()
