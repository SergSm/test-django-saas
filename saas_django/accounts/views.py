from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from . import serializers


User = get_user_model()


# by inheriting from generics.CreateAPIView we block
# other(?) ways to list or update accounts
class AccountCreate(generics.CreateAPIView):
    name = 'account-create'
    serializer_class = serializers.AccountSerializer


class UserList(generics.ListCreateAPIView):
    name = 'user-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        company_id = self.request.user.company_id
        serializer.save(company_id=company_id)

    # Overrides the default method
    def get_queryset(self):
        # !!!Ensure that the users belong to the company of the user that is making the request
        company_id = self.request.user.company_id
        return super().get_queryset().filter(company_id=company_id)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'user-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        # Ensure that the user belongs to the company of the user that is making the request
        # Note that this method is identical to the one in `UserList`
        company_id = self.request.user.company_id
        return super().get_queryset().filter(company_id=company_id)


class CompanyDetail(generics.RetrieveUpdateAPIView):
    name = 'company-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = serializers.CompanySerializer

    def get_object(self):
        # Ensure that users can only see the company that they belong to
        return self.request.user.company
