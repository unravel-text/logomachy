from django.views import generic as view


class CreditsView(view.TemplateView):
    template_name = 'logomachy/about/credits.html'
