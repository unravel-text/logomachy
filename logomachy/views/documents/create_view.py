from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic as view
import logomachy.models as app_models


@method_decorator(login_required, name='dispatch')
class CreateView(view.CreateView):
    model = app_models.Document
    template_name = 'logomachy/documents/create.html'
    fields = ['name', 'title', 'description', 'category', 'tags']

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        return super().form_valid(form)
