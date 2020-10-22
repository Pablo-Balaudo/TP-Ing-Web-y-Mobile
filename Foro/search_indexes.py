from haystack import indexes

from Foro.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='text')
    date_posted = indexes.DateTimeField(model_attr='date_posted')
    author = indexes.CharField(model_attr='author')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        # Get all the posts
        return self.get_model().objects.all()
