from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Organization)
admin.site.register(models.Picture)
admin.site.register(models.Sport)
admin.site.register(models.Member)