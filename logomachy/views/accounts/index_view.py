from django.views import generic as view
import logomachy.models as app_models
from django.conf import settings
from django.apps import apps as django_apps


class IndexView(view.ListView):
    model = django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
    template_name = 'logomachy/accounts/index.html'
