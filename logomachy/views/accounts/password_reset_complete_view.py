from django.contrib.auth import views


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'logomachy/accounts/password_reset_complete.html'
