from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, SuspiciousOperation
from django.http import Http404
from django.views import generic as view


class ProfileView(view.TemplateView):
    template_name = 'logomachy/accounts/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # The profile can show the current user's profile, or the profile for another user.
        # Check if there is a 'username' in the context - this is the username of the user to display
        username = context.get('username')

        if username:
            try:
                user = get_user_model().objects.get(username=username)
            except ObjectDoesNotExist:
                raise Http404(f'User with name "{username}" does not exist.')
        else:
            user = self.request.user

        context['displayed_user'] = user
        context['own_profile'] = (username is not None and username == user.username) or True

        # raise Http404
        # raise PermissionDenied('testing')
        # raise SuspiciousOperation
        # raise ValueError

        return context
