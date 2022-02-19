from rest_framework import serializers

from . import models


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = ['image', 'club', ]
        extra_kwargs = {'club': {'write_only': True}}


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sport
        fields = '__all__'
