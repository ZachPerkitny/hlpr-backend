from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    User Registration Serializer
    """
    class Meta:
        model = User
        fields = ('email', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserListSerializer(serializers.ModelSerializer):
    """
    User List Serializer
    """
    class Meta:
        model = User
        fields = ('username', 'id',)


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User Detail Serializer - username, email and id cannot be updated.
    """
    avatar = Base64ImageField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'first_name', 'last_name', 'alliedmodders', 'avatar',
                  'github', 'twitter',)
        read_only_fields = ('username', 'email', 'id',)


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
