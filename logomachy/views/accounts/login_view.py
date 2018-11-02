from django.contrib.auth import views


class LoginView(views.LoginView):
    template_name = 'logomachy/accounts/login.html'
