from django.views import generic as view
import logomachy.models as app_models


class UpdateView(view.UpdateView):
    model = app_models.Document
    template_name = 'logomachy/documents/update.html'
    slug_url_kwarg = 'name'
    slug_field = 'name'
    fields = ['name', 'title', 'description', 'category', 'tags']
    context_object_name = 'document'

    def form_valid(self, form):
        form.instance.updated_user = self.request.user
        return super().form_valid(form)
