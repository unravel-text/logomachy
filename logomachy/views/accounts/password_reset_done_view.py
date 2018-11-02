from django.contrib.auth import views


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'logomachy/accounts/password_reset_done.html'
