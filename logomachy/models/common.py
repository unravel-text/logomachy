from django.conf import settings
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Common(models.Model):
    """
    An abstract base model that provides common attributes and behaviour.
    """

    created_date = models.DateTimeField(
        auto_now_add=True,
        help_text='The date this record was created.')
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_created', related_query_name='%(app_label)s_%(class)s_creators',
        help_text='The user that created this record.')

    updated_date = models.DateTimeField(
        auto_now=True,
        help_text='The date this record was lat updated.')
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_updated', related_query_name='%(app_label)s_%(class)s_updaters',
        help_text='The user that last updated this record.')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save the current instance, and add LogEntry log_action.
        """

        request = self._get_request_user(**kwargs)
        if self.pk is None:
            # add / create
            msg = [{'added': {
                'name': str(self._meta.verbose_name),
                'object': str(self),
            }}]
            self._log_addition(request, self, msg)
            self.created_user = request.user
        else:
            # update / modify - fields: list of field names
            msg = [{'added': {
                'name': str(self._meta.verbose_name),
                'object': str(self),
                'fields': sorted(f.name for f in self._meta.get_fields()),
            }}]
            self._log_change(request, self, msg)
            self.updated_user = request.user

        # save object
        if 'request' in kwargs:
            kwargs.pop('request')
        super(Common, self).save(*args, **kwargs)

        # TODO: include user in save

    def delete(self, *args, **kwargs):
        """
        Delete the current instance, and add LogEntry log_action.
        """

        request = self._get_request_user(**kwargs)
        self._log_deletion(request, self, str(self))

        # delete object
        if 'request' in kwargs:
            kwargs.pop('request')
        return super(Common, self).delete(*args, **kwargs)

    def _get_request_user(self, **kwargs):
        """
        Get the user from the current request.
        """

        request = kwargs.get('request')
        if not request or not request.user or request.user.is_anonymous:
            raise ValueError(
                'Must pass request with valid logged in user for creating, updating, or deleting a model instance.')
        return request

    def _log_addition(self, request, obj, message):
        """
        Log that an object has been successfully added. Creates an admin LogEntry object.
        """

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=ADDITION,
            change_message=message,
        )

    def _log_change(self, request, obj, message):
        """
        Log that an object has been successfully changed. Creates an admin LogEntry object.
        """

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=CHANGE,
            change_message=message,
        )

    def _log_deletion(self, request, obj, object_repr):
        """
        Log that an object will be deleted. Creates an admin LogEntry object.

        Note that this method must be called before the deletion.
        """

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )
