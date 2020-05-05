from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.settings import api_settings
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, UntypedToken
from drf_base64.fields import Base64ImageField
from . import models


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = ['image', 'club', ]
        extra_kwargs = {'club': {'write_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(required=False, max_length=None, use_url=True)

    class Meta:
        model = models.Profile
        fields = '__all__'
        read_only_fields = ['id', 'owner']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = models.User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'profile']


class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.CharField(min_length=3, max_length=20)
    last_name = serializers.CharField(min_length=3, max_length=50)

    class Meta:
        model = models.User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'email', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        user = super(RegisterSerializer, self).create(validated_data={
            'username': validated_data['username'],
            'email': validated_data['email'],
            'password': validated_data['password'],
        })

        profile = models.Profile(
            owner=user, first_name=validated_data['first_name'], last_name=validated_data['last_name'])

        profile.save()

        return user

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data


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


class PichangaSerializer(serializers.ModelSerializer):
    pictures = ImageUrlField(many=True, read_only=True)
    members = MemberSerializer(many=True, read_only=True)
    sport = SportSerializer()
    logo = Base64ImageField(required=False, max_length=None, use_url=True)

    class Meta:
        model = models.Pichanga
        fields = '__all__'

    def create(self, validated_data):
        sport = models.Sport.objects.get(name=validated_data['sport']['name'])
        validated_data['sport'] = sport
        return super().create(validated_data)
