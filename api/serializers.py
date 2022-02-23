from rest_framework import serializers

from . import models


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = ['id', 'image',]
        # extra_kwargs = {'org': {'write_only': True}}

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sport
        fields = '__all__'
