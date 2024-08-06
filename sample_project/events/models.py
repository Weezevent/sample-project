from django.db import models

from sample_project.organizations.models import Organization


class Event(models.Model):
    FESTIVAL = 'festival'
    CONCERT = 'concert'
    CONFERENCE = 'conference'

    TYPE_CHOICES = [
        (CONFERENCE, CONFERENCE),
        (FESTIVAL, FESTIVAL),
        (CONCERT, CONCERT)
    ]

    type = models.CharField(choices=TYPE_CHOICES, default=FESTIVAL, max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
