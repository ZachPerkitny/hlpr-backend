import os
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from .choices import CategoryChoices, GameChoices, ModChoices
from .fields import VersionNumberField, VersionNumber


def version_default():
    """
    Default wrapper for version
    """
    return VersionNumber(1,)


class Plugin(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(editable=False, unique=True)
    description = models.TextField(max_length=4096)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='plugin_author'
    )
    collaborators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='plugin_collaborator',
        blank=True
    )
    created = models.DateTimeField(editable=False)
    last_updated = models.DateTimeField(editable=False)
    repository = models.URLField(blank=True)
    category = models.CharField(
        max_length=24,
        choices=CategoryChoices.choices,
        default=CategoryChoices.general_purpose
    )
    game = models.CharField(
        max_length=16,
        choices=GameChoices.choices,
        default=GameChoices.any
    )
    mod = models.CharField(
        max_length=12,
        choices=ModChoices.choices,
        default=ModChoices.sourcemod
    )

    class Meta:
        verbose_name = 'Plugin'
        verbose_name_plural = 'Plugins'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # generate slug on creation
            self.slug = slugify(self.name)
            # set created time
            self.created = timezone.now()
        # update last_updated time
        self.last_updated = timezone.now()
        return super(Plugin, self).save(*args, **kwargs)


class Version(models.Model):
    version = VersionNumberField(default=version_default)
    plugin = models.ForeignKey(
        Plugin,
        on_delete=models.CASCADE,
        related_name='versions'
    )

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'

    def __str__(self):
        return str(self.version)


class File(models.Model):
    file = models.FileField()
    version = models.ForeignKey(
        Version,
        on_delete=models.CASCADE,
        related_name='files'
    )

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return os.path.basename(self.file.name)
