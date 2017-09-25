from datetime import datetime
from rest_framework_jwt.settings import api_settings
from .serializers import UserDetailSerializer


def jwt_payload_handler(user):
    """
    Custom Payload Handler
    """
    return {
        'user_id': user.pk,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Custom Response Payload Handler
    """
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data
    }
