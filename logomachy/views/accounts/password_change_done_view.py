from django.contrib.auth import views


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'logomachy/accounts/password_change_done.html'
