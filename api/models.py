from django.db import models
from .mixins import AutoCreatedUpdatedMixin

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Organization(AutoCreatedUpdatedMixin):
    name = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=5)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Member(AutoCreatedUpdatedMixin):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    org = models.ForeignKey('Pichanga', on_delete=models.CASCADE, related_name='members')
    nickname = models.CharField(max_length=16)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname


class Picture(models.Model):
    image = models.ImageField(blank=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return self.image.name
