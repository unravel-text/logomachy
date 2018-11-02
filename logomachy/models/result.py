import uuid

from django.contrib.postgres import fields as pg_fields
from django.core.serializers import json as json_serializers
from django.db import models

import logomachy.models as app_models


class Result(app_models.Common):
    """
    The output from processing one or more documents.
    For each revision, only the most recent output is kept for each processor.
    """

    PROCESSOR_TYPE_SOURCE = 'source'
    PROCESSOR_TYPE_PARSE = 'parse'
    PROCESSOR_TYPE_INTERPRET = 'interpret'
    PROCESSOR_TYPE_ANALYSE = 'analyse'

    PROCESSOR_TYPES = (
        (PROCESSOR_TYPE_SOURCE, 'Source'),
        (PROCESSOR_TYPE_PARSE, 'Parse'),
        (PROCESSOR_TYPE_INTERPRET, 'Interpret'),
        (PROCESSOR_TYPE_ANALYSE, 'Analyse'),
    )

    name = models.UUIDField(
        default=uuid.uuid4, null=False, blank=False, editable=False, unique=True,
        help_text='A generated, unique name for a result.')
    processor_name = models.SlugField(
        max_length=200, null=False, blank=False, unique=True,
        help_text='The unique name of the processor that output this result.')
    processor_version = models.CharField(
        max_length=100, null=False, blank=False,
        help_text='The version of the processor.')
    processor_type = models.CharField(
        max_length=100, null=False, blank=False, choices=PROCESSOR_TYPES,
        help_text='The type of processor.')
    started_date = models.DateTimeField(
        help_text='The date the processing started.')
    output = pg_fields.JSONField(
        encoder=json_serializers.DjangoJSONEncoder,
        help_text='The output from the processor.')

    revisions = models.ManyToManyField(
        app_models.Revision, related_name='results',
        help_text='The revisions used as input to the processor.')

    class Meta:
        verbose_name = 'result'
        verbose_name_plural = 'Results'

    def __str__(self):
        return f'{self.processor_name} ({self.processor_version})'
