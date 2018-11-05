from django.conf import settings
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
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
        help_text='The date this record was last updated.')
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_updated', related_query_name='%(app_label)s_%(class)s_updaters',
        help_text='The user that last updated this record.')

    # NOTE: for now, records are actually deleted - this means the deleted user is never actually saved.
    # this is used for logging actions.
    # this could be used for archiving records if that is needed
    deleted_date = models.DateTimeField(
        blank=True, null=True,
        help_text='The date this record was delete.')
    deleted_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_deleted', related_query_name='%(app_label)s_%(class)s_deleters',
        help_text='The user that deleted this record.')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save the current instance, and add LogEntry log_action.
        """

        if self.pk is None:
            # do the save
            super(Common, self).save(*args, **kwargs)

            # add / create
            self._common_model_create()
        else:
            # update / modify - fields: list of field names
            self._common_model_update()

            # do the save
            super(Common, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Delete the current instance, and add LogEntry log_action.
        """

        self._common_model_delete()

        # do the delete
        return super(Common, self).delete(*args, **kwargs)

    def _common_model_create(self):
        if self.created_user is None or not self.created_user.pk:
            raise PermissionDenied("A valid user is required to create a new {}".format(self._meta.object_name))
        if not self.pk:
            raise ObjectDoesNotExist("Save the model before recording a log action.")

        msg = [{
            'added': {
                'name': str(self._meta.verbose_name),
                'object': str(self),
            }
        }]
        self._common_model_log_addition(self.created_user, self, msg)

    def _common_model_update(self):
        if self.updated_user is None or not self.updated_user.pk:
            raise PermissionDenied("A valid user is required to update an existing {}".format(self._meta.object_name))
        if not self.pk:
            raise ObjectDoesNotExist("Save the model before recording a log action.")

        msg = [{
            'added': {
                'name': str(self._meta.verbose_name),
                'object': str(self),
                'fields': sorted(f.name for f in self._meta.get_fields()),
            }}]
        self._common_model_log_change(self.updated_user, self, msg)

    def _common_model_delete(self):
        if self.deleted_user is None or not self.deleted_user.pk:
            raise PermissionDenied("A valid user is required to delete an existing {}".format(self._meta.object_name))
        if not self.pk:
            raise ObjectDoesNotExist("Save the model before recording a log action.")

        self._common_model_log_deletion(self.deleted_user, self, str(self))

    def _common_model_log_addition(self, user, obj, message):
        """
        Log that an object has been successfully added. Creates an admin LogEntry object.
        """

        return LogEntry.objects.log_action(
            user_id=user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=ADDITION,
            change_message=message,
        )

    def _common_model_log_change(self, user, obj, message):
        """
        Log that an object has been successfully changed. Creates an admin LogEntry object.
        """

        return LogEntry.objects.log_action(
            user_id=user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=CHANGE,
            change_message=message,
        )

    def _common_model_log_deletion(self, user, obj, object_repr):
        """
        Log that an object will be deleted. Creates an admin LogEntry object.

        Note that this method must be called before the deletion.
        """

        return LogEntry.objects.log_action(
            user_id=user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )
