from django.views import generic as view
import logomachy.models as app_models


class IndexView(view.ListView):
    model = app_models.Document
    template_name = 'logomachy/documents/index.html'
    context_object_name = 'documents'
