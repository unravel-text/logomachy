from django.views import generic as view


class TermsView(view.TemplateView):
    template_name = 'logomachy/about/terms.html'
