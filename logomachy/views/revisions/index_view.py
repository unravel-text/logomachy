from django.views import generic as view
import logomachy.models as app_models


class IndexView(view.ListView):
    model = app_models.Revision
    template_name = 'logomachy/revisions/index.html'
    context_object_name = 'revisions'
