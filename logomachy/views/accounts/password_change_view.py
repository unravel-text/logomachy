from django.contrib.auth import views


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'logomachy/accounts/password_change.html'
