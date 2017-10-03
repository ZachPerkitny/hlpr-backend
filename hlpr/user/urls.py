"""
User URL Configuration
"""

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import (UserCreateView, UserDetailView, UserListView, UserUpdateView,
                    ChangePasswordView, CheckUsernameAvailabilityView)

urlpatterns = [
    url(r'^login/$', obtain_jwt_token),
    url(r'^register/$', UserCreateView.as_view()),
    url(r'^refresh-token/$', refresh_jwt_token),
    url(r'^verify-token/$', verify_jwt_token),
    url(r'^accounts/$', UserListView.as_view()),
    url(r'^accounts/update/$', UserUpdateView.as_view()),
    url(r'^accounts/change_password/$', ChangePasswordView.as_view()),
    url(r'^accounts/(?P<id>\d+)/$', UserDetailView.as_view()),
    url(r'^accounts/check_availability/(?P<username>[\w\.@+-]+)/',
        CheckUsernameAvailabilityView.as_view()),
]
