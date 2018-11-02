from django.views import generic as view
import logomachy.models as app_models


class UpdateView(view.UpdateView):
    model = app_models.Document
    template_name = 'logomachy/documents/update.html'
