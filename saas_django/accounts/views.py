from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth import get_user_model

# new imports
#import core.views
from core.views import CompanySafeViewMixin
#from saas_django.core.views import CompanySafeViewMixin
from . import serializers


User = get_user_model()


# by inheriting from generics.CreateAPIView we block
# other(?) ways to list or update accounts
class AccountCreate(generics.CreateAPIView):
    name = 'account-create'
    serializer_class = serializers.AccountSerializer


# Added CompanySafeViewMixin
class UserList(CompanySafeViewMixin, generics.ListCreateAPIView):
    name = 'user-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    # removed get_queryset and perform_create


# Added CompanySafeViewMixin
class UserDetail(CompanySafeViewMixin, generics.RetrieveUpdateDestroyAPIView):
    name = 'user-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    # Removed get_queryset


class CompanyDetail(generics.RetrieveUpdateAPIView):
    name = 'company-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = serializers.CompanySerializer

    def get_object(self):
        # Ensure that users can only see the company that they belong to
        return self.request.user.company
