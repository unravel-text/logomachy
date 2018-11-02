from django.views import generic as view
import logomachy.models as app_models


class IndexView(view.TemplateView):
    template_name = 'logomachy/index.html'
