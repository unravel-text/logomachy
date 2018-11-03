from django.views import generic as view


class PrivacyView(view.TemplateView):
    template_name = 'logomachy/about/privacy.html'
