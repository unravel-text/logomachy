from django.db import models
from django.utils.text import slugify

import logomachy.models as app_models
from logomachy import utils as app_utils


class Document(app_models.Common, app_utils.ModeratorMixin):
    """
    A company, government, or other entity's law, policy, or legal document.
    """

    CATEGORY_LAW = 'law'
    CATEGORY_TOS = 'tos'
    CATEGORY_EULA = 'eula'
    CATEGORY_PRIVACY = 'privacy'

    CATEGORIES = (
        (CATEGORY_LAW, 'Law'),
        (CATEGORY_TOS, 'Terms of Service'),
        (CATEGORY_EULA, 'End User License Agreement'),
        (CATEGORY_PRIVACY, 'Privacy Policy')
    )

    name = models.SlugField(
        max_length=100, null=False, blank=False, unique=True,
        help_text='The simple and unique name of this document. '
                  'A combination of creator name and document title is recommended.')
    title = models.CharField(
        max_length=300, null=False, blank=False, unique=True, help_text='The title of this document.')
    description = models.TextField(
        max_length=1000, null=True, blank=True, help_text='A summary of the content of this document.')
    category = models.CharField(
        max_length=50, null=False, blank=False, choices=CATEGORIES, help_text='The category of this document.')

    tags = models.ManyToManyField(
        app_models.Tag, blank=True, related_name='documents',
        help_text='The tags applied to this revision of a document, '
                  'for example indicating a geographic or social region, author or creator, or application scope.')

    # FK - one to many: revisions

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return f'{self.name} "{self.title}"'

    def save(self, *args, **kwargs):
        """
        Save this object.
        Create a name based on the title if this object has not yet been saved or if there is no name.
        """
        if self.pk is None or self.name is None:
            self.name = slugify(self.title)

        super(Document, self).save(*args, **kwargs)
