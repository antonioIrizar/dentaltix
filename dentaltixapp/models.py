"""Models for dentaltixapp"""
from __future__ import unicode_literals

from django.db import models


class ProgrammingLanguage(models.Model):
    """Model for programming language"""
    # name is unique because name of programming languages are unique
    # by default charfield can't empty. It's nice
    name = models.CharField(unique=True, max_length=50)

    def __unicode__(self):
        """ unicode representation """
        return self.name


class Framework(models.Model):
    """Model for frameworks"""
    # relationship to programming language. It is one to many. One programming laguage can have many frameworks.
    programming_language = models.ForeignKey(ProgrammingLanguage, related_name='frameworks', blank=True, null=True)
    # name isn't unique because I can have frameworks with same name to different programming language
    name = models.CharField(max_length=50)

    class Meta:
        # I order by name's frameworks. Because I see in json It is order or it is only a coincidence :).
        unique_together = ['programming_language', 'name']
        ordering = ['name']

    def __unicode__(self):
        return self.name
