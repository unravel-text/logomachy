from django.contrib.auth import views


class LogoutView(views.LogoutView):
    template_name = 'logomachy/accounts/logout.html'
