from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView,
                                     GenericAPIView)
from rest_framework.views import Response, APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from .models import User
from .serializers import (UserCreateSerializer, UserDetailSerializer, UserListSerializer,
                          ChangePasswordSerializer)


class UserCreateView(CreateAPIView):
    """
    User Registration
    """
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        """
        Overrides the default create method. Returns a JWT token,
        so the user is automatically logged in after registration.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
        payload = jwt_payload_handler(serializer.instance)
        token = jwt_encode_handler(payload)
        return Response(
            jwt_response_payload_handler(token, serializer.instance),
            status=status.HTTP_201_CREATED
        )


class UserListView(ListAPIView):
    """
    Gets a list of users
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    """
    Gets a specific user by filtering against its id
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'


class UserUpdateView(UpdateAPIView):
    """
    Updates the user's account
    """
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ChangePasswordView(GenericAPIView):
    """
    Updates a user's password
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "New password has been saved."})


class CheckUsernameAvailabilityView(APIView):
    """
    Checks if a username is available
    """
    def get(self, request, username, format=None):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'available': True})
        return Response({'available': False})
