from django.views import generic as view
import logomachy.models as app_models


class CreateView(view.CreateView):
    model = app_models.Revision
    template_name = 'logomachy/revisions/create.html'
    fields = ['language', 'country', 'source_url', 'source_value', 'source_media_type',
              'creator_url', 'content_raw',  'document']
