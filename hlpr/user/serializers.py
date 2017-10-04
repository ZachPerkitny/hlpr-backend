from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .gravatar import get_gravatar_url
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    User Registration Serializer
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)

    def validate_password(self, value):
        """
        Ensures valid password (min length, etc, see settings)
        """
        validate_password(value)
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserListSerializer(serializers.ModelSerializer):
    """
    User List Serializer
    """
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'id', 'avatar',)

    def get_avatar(self, obj):
        return get_gravatar_url(obj.email)


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User Detail Serializer - username, email and id cannot be updated.
    """
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'first_name', 'last_name', 'alliedmodders', 'avatar',
                  'github', 'twitter',)
        read_only_fields = ('username', 'email', 'id',)

    def get_avatar(self, obj):
        return get_gravatar_url(obj.email)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for updating a user's password.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        """
        Ensures old password is correct.
        """
        if not self.instance.check_password(value):
            raise serializers.ValidationError('Invalid Password.')
        return value

    def update(self, instance, validated_data):
        """
        Updates Instance Password
        """
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
