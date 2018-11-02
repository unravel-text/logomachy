from django.views import generic as view
import logomachy.models as app_models


class CreateView(view.CreateView):
    model = app_models.Document
    template_name = 'logomachy/documents/create.html'
    fields = ['name', 'title', 'description', 'category', 'tags']
