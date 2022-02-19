from rest_framework import serializers
from drf_base64.fields import Base64ImageField
from . import models


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = ['image', 'club', ]
        extra_kwargs = {'club': {'write_only': True}}


class ImageUrlField(serializers.RelatedField):
    def to_representation(self, isinstance):
        url = isinstance.image.url
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sport
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    pictures = ImageUrlField(many=True, read_only=True)
    members = MemberSerializer(many=True, read_only=True)
    sport = SportSerializer()
    logo = Base64ImageField(required=False, max_length=None, use_url=True)

    class Meta:
        model = models.Organization
        fields = '__all__'

    def create(self, validated_data):
        sport = models.Sport.objects.get(name=validated_data['sport']['name'])
        validated_data['sport'] = sport
        return super().create(validated_data)
