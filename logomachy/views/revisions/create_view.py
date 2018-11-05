from django.urls import reverse
from django.views import generic as view
import logomachy.models as app_models


class CreateView(view.CreateView):
    model = app_models.Revision
    template_name = 'logomachy/revisions/create.html'
    fields = ['language', 'country', 'source_url', 'source_value', 'source_media_type',
              'creator_url', 'content_raw',  'document']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['document_name'] = self.kwargs['name']

        return context

    def get_initial(self):
        initial = super(CreateView, self).get_initial()
        initial['document'] = app_models.Document.objects.get(name=self.kwargs['name'])
        return initial

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        return super().form_valid(form)

