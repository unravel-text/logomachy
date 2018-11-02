from django.contrib.auth import views


class PasswordResetView(views.PasswordResetView):
    template_name = 'logomachy/accounts/password_reset.html'
