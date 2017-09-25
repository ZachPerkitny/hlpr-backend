from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'email': {
                'required': True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'id',)


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'id', 'first_name', 'last_name', 'alliedmodders', 'avatar', 'bio',
                  'github', 'twitter',)
