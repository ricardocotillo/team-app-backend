from django.db import models

from api.mixins import AutoCreatedUpdatedMixin

# Create your models here.
class Organization(AutoCreatedUpdatedMixin):
    name = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=5)
    sport = models.ForeignKey('api.Sport', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Member(AutoCreatedUpdatedMixin):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    nickname = models.CharField(max_length=16)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname