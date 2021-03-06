from rest_framework import serializers
from core.serializers import CompanySafeSerializerMixin


#from .models import UserMessage

from .models import UserMessage as UM
#from .models import UserMessage


# Changed line (adds the CompanySafeSerializerMixin)
class UserMessageSerializer(CompanySafeSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UM
        fields = (
            'id',
            'url',
            'from_user',
            'to_user',
            'text',
            'date',
        )

        read_only_fields = (
            'from_user',
        )