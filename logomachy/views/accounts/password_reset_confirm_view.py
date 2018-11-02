from django.contrib.auth import views


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'logomachy/accounts/password_reset_confirm.html'
