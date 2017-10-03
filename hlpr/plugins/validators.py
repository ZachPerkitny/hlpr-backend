import os
from django.core.exceptions import ValidationError


def validate_file_extension(file):
    """
    Ensures the file is an archive (.zip)
    """
    ext = os.path.splitext(file.name)[1]
    if ext.lower() != '.zip':
        raise ValidationError('Expected an archive file (.zip).')
