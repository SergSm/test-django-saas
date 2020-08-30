from rest_framework import permissions
from rest_framework import generics

from . import serializers
from .models import UserMessage


class UserMessageList(generics.ListCreateAPIView):
    name = 'usermessage-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        company_id = user.company_id
        # Added from_user
        serializer.save(company_id=company_id, from_user=user)

    def get_queryset(self):
        # Changed this to use the UserMessageManager's method
        return UserMessage.objects.get_for_user(self.request.user)


class UserMessageDetail(generics.RetrieveAPIView):
    name = 'usermessage-detail'
    permission_classes = (
       permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer

    def get_queryset(self):
        # Changed this to use the UserMessageManager's method
        return UserMessage.objects.get_for_user(self.request.user)