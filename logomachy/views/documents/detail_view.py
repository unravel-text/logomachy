from django.views import generic as view
import logomachy.models as app_models


class DetailView(view.DetailView):
    model = app_models.Document
    template_name = 'logomachy/documents/detail.html'
