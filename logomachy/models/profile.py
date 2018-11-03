from django.conf import settings
from django.db import models

import logomachy.models as app_models


class Profile(app_models.Common):
    """
    Profile information for a user.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        help_text='This profile is associated with this user.'
    )

    locale_name = models.CharField(
        max_length=10, null=True, blank=True,
        help_text='Select your locale.')
    language_code = models.CharField(
        max_length=10, null=True, blank=True,
        help_text='Select your language.')

    time_zone_name = models.CharField(
        max_length=200, null=True, blank=True,
        help_text='Select your time zone.')
    time_zone_code = models.CharField(
        max_length=10, null=True, blank=True,
        help_text='Select your time zone.')
    time_zone_offset = models.CharField(
        max_length=50, null=True, blank=True,
        help_text='Select your time zone.')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user} profile'

    def save(self, *args, **kwargs):
        """
        Save this object.
        Create a name based on the title if this object has not yet been saved or if there is no name.
        """
        if self.pk is None or self.name is None:
            self.name = slugify(self.title)

        super(Document, self).save(*args, **kwargs)