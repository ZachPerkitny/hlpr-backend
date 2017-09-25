from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from .models import User
from .serializers import UserCreateSerializer, UserDetailSerializer, UserListSerializer


class UserCreateView(CreateAPIView):
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
        payload = jwt_payload_handler(serializer.instance)
        token = jwt_encode_handler(payload)
        return Response(
            {
                'token': token
            },
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
