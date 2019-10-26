from django.contrib.auth import authenticate, login
from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'rating')
        read_only_fields = ('rating',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        self.user = authenticate(username=username, password=password)
        if not self.user:
            raise serializers.ValidationError('Login or password is invalid')

        return attrs

    def save(self, **kwargs):
        login(self.context['request'], self.user)
        return self.user
