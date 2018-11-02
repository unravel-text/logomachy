from django.views import generic as view
import logomachy.models as app_models


class DetailView(view.DetailView):
    model = app_models.Revision
    template_name = 'logomachy/revisions/detail.html'
