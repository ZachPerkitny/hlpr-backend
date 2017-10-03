from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from .choices import CategoryChoices, GameChoices, ModChoices
from .fields import VersionNumberField, VersionNumber
from .validators import validate_file_extension


class Plugin(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(editable=False, unique=True)
    summary = models.TextField(max_length=140)
    description = models.TextField(max_length=4096)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='plugins'
    )
    collaborators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='+',
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
        default=GameChoices.any_game
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
            # set created time
            self.created = timezone.now()
        # generate new slug on creation/update
        self.slug = slugify(self.name)
        # update last_updated time
        self.last_updated = timezone.now()
        return super(Plugin, self).save(*args, **kwargs)


def version_default():
    # Default wrapper for version
    return VersionNumber(1,)


def file_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/plugins/<plugin_name>/<version>/<filename>
    return 'plugins/%s/%s/%s' % (instance.plugin.slug, instance.version, filename)


class Version(models.Model):
    version = VersionNumberField(default=version_default)
    plugin = models.ForeignKey(
        Plugin,
        on_delete=models.CASCADE,
        related_name='versions'
    )
    archive = models.FileField(
        upload_to=file_directory_path,
        validators=[validate_file_extension]
    )

    class Meta:
        unique_together = ('version', 'plugin')
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'

    def __str__(self):
        return str(self.version)
