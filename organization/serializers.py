from rest_framework import serializers
from drf_base64.fields import Base64ImageField

from api.fields import ImageUrlField
from api.serializers import SportSerializer
from api.models import Sport

from .models import Organization, Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    pictures = ImageUrlField(many=True, read_only=True)
    members = MemberSerializer(many=True, read_only=True)
    sport = SportSerializer()
    logo = Base64ImageField(required=False, max_length=None, use_url=True)

    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        sport = Sport.objects.get(name=validated_data['sport']['name'])
        validated_data['sport'] = sport
        return super().create(validated_data)