from django.views import generic as view
import logomachy.models as app_models


class DetailView(view.DetailView):
    model = app_models.Revision
    template_name = 'logomachy/revisions/detail.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'
    context_object_name = 'revision'
