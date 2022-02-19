from django.db import models
from .mixins import AutoCreatedUpdatedMixin

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Picture(models.Model):
    image = models.ImageField(blank=True)
    org = models.ForeignKey('organization.Organization', on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return self.image.name
