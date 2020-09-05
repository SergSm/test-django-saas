from django.contrib.auth import get_user_model
from django.db import models

# new import
from django.db.models import Q

from core.models import CompanyRelatedModel


User = get_user_model()


# new class
class UserMessageManager(models.Manager):

    def get_for_user(self, user):
        """Retrieves all messages that a user either sent or received"""
        return self.all().filter(company_id=user.company_id).filter(Q(from_user=user) | Q(to_user=user))


# model inherits id and company from CompanyRelatedModel
class UserMessage(CompanyRelatedModel):
    text = models.TextField('message', blank=False, null=False)
    date = models.DateTimeField('date', auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)

    # New model manager
    objects = UserMessageManager()

    class Meta:
        db_table = 'user_messages'
        ordering = ['date']



