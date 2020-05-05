from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .mixins import AutoCreatedUpdatedMixin


class Profile(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=12)

    def __str__(self):
        return self.owner.username


class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(AutoCreatedUpdatedMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16)
    active = models.BooleanField()
    admin = models.BooleanField(default=False)
    pichanga = models.ForeignKey(
        'Pichanga', on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        if self.nickname:
            return self.nickname
        return self.user.username


class Pichanga(AutoCreatedUpdatedMixin):
    name = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=5)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(blank=True)
    club = models.ForeignKey(
        Pichanga, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return self.image.name
