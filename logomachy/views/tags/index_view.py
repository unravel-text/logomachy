from django.views import generic as view
import logomachy.models as app_models


class IndexView(view.ListView):
    model = app_models.Revision
    template_name = 'logomachy/tags/index.html'
