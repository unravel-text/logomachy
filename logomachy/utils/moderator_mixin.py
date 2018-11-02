from django.conf import settings
from django.db import models


class ModeratedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(moderated_date_isnull=False)


class ModeratorMixin:
    """
    Mixin that adds requirement for moderation to a Django model.
    """

    moderated_date = models.DateTimeField(
        blank=True, null=True,
        help_text='The date this record was moderated.')
    moderated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_moderated', related_query_name='%(app_label)s_%(class)s_moderators',
        help_text='The user that moderated this record.')

    class Meta:
        default_manager_name = ModeratedManager
