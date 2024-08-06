from django.db import models


class Organization(models.Model):
    name = models.CharField()
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
