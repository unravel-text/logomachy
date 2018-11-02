import uuid

from django.db import models

import logomachy.models as app_models
from logomachy import utils as app_utils


class Revision(app_models.Common, app_utils.ModeratorMixin):
    """
    A revision of a document.
    """

    SOURCE_VALUE_FILE = 'file'
    SOURCE_VALUE_URL = 'url'
    SOURCE_VALUE_STRING = 'url'

    SOURCE_VALUES = (
        (SOURCE_VALUE_FILE, 'File'),
        (SOURCE_VALUE_URL, 'URL'),
        (SOURCE_VALUE_STRING, 'String'),
    )

    # see Common.created_date for date_collected
    # see Common.updated_date for date_modified

    name = models.UUIDField(
        default=uuid.uuid4, null=False, blank=False, editable=False, unique=True,
        help_text='A generated, unique name for a revision.')

    language = models.CharField(
        max_length=10, null=False, blank=False,
        help_text='The language of this revision of the document.')
    country = models.CharField(
        max_length=10, null=False, blank=False,
        help_text='The country locale of this revision of the document.')

    source_url = models.URLField(
        max_length=2000, null=True, blank=True,
        help_text='Link to a website where the latest document can be obtained.')
    source_value = models.CharField(
        max_length=2000, null=False, blank=False, choices=SOURCE_VALUES,
        help_text='The source of this revision of the document.')
    source_media_type = models.CharField(
        max_length=100, null=True, blank=True,
        help_text='The source media type of this revision of the document.')

    creator_url = models.URLField(
        max_length=2000, null=True, blank=True,
        help_text='Link to a website of the creator of this revision of the document.')

    content_raw = models.TextField(
        null=False, blank=False,
        help_text='Raw content of this revision of the document.')
    content_normalised = models.TextField(
        null=True, blank=True,
        help_text='Normalised content of this revision of the document.')

    document = models.ForeignKey(
        app_models.Document, on_delete=models.CASCADE, related_name='revisions',
        help_text='This revision is a version of this document.')

    # FK - many to many: results

    class Meta:
        verbose_name = 'Revision'
        verbose_name_plural = 'Revisions'

    def __str__(self):
        return f'{self.document.name} [{self.name}] ({self.created_date})'
