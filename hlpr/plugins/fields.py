import struct
from django.db import models


class VersionNumber(object):

    def __init__(self, major, minor=0, patch=0, build=0):
        self.version = (int(major), int(minor), int(patch), int(build))
        if any([x < 0 or x > 255 for x in self.version]):
            raise ValueError('Version number <major.minor.patch.build> components must be in the '
                             'inclusive range 0, 255')

    def __int__(self):
        """
        Returns a 32 bit signed representation of a VersionNumber object
        """
        major, minor, patch, build = self.version
        num = (major << 24) | (minor << 16) | (patch << 8) | build
        return num - 2**31

    def __str__(self):
        """
        Returns a string representation of a VersionNumber object in the form:
        'major.minor.patch.build'
        """
        ei = 3 if self.version[3] else 2
        return '.'.join([str(x) for x in self.version[:ei + 1]])

    def __repr__(self):
        return '<%s.%s%s>' % (
            self.__class__.__name__,
            self.__class__.__module__,
            repr(self.version)
        )


class VersionNumberField(models.Field):

    description = "A project's version number <major.minor.patch.build>"

    def get_internal_type(self):
        return 'IntegerField'

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def to_python(self, value):
        """
        Converts a tuple, string or integer into a VersionNumber.
        """
        if isinstance(value, VersionNumber) or value is None:
            return value
        if isinstance(value, tuple):
            return VersionNumber(*value)
        if isinstance(value, str):
            return VersionNumber(*value.split('.'))
        packed = [b for b in struct.pack('>I', value + 2**31)]
        return VersionNumber(*packed)

    def get_prep_value(self, value):
        """
        Converts a VersionNumber object or a tuple to its signed
        integer representation (prepared for use as a query parameter).
        """
        if isinstance(value, VersionNumber):
            return int(value)
        if isinstance(value, tuple):
            return int(VersionNumber(*value))
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            return int(VersionNumber(*value.split('.')))
