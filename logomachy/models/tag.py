from django.db import models
from django.urls import reverse_lazy

import logomachy.models as app_models


class Tag(app_models.Common):
    """
    A desciptive text label that conveys some information.
    """

    name = models.SlugField(
        max_length=100, null=False, blank=False, unique=True,
        help_text='The simple name of this tag.')
    title = models.CharField(
        max_length=700, null=False, blank=False,
        help_text='A verbose name for this tag.')
    description = models.TextField(
        null=True, blank=True,
        help_text='A description of this tag.')

    # FK - many to many: documents

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return '{} "{}"'.format(self.name, self.title)

    def get_absolute_url(self):
        return reverse_lazy('logomachy:tags:detail', kwargs={'name': self.name})
