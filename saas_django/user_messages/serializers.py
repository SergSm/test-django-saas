from rest_framework import serializers
# Changed line (adds the import of CompanySafeSerializerMixin)
from core.serializers import CompanySafeSerializerMixin
from .models import UserMessage


# Changed line (adds the CompanySafeSerializerMixin)
class UserMessageSerializer(CompanySafeSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMessage
        fields = (
            'id',
            'url',
            'from_user',
            'to_user',
            'text',
            'date',
        )