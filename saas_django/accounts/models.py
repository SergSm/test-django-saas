import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models, transaction


class CompanyManager(models.Manager):
    """Manager for the Company model. Also handles the account creation
    Provides user creation only with the company"""

    # "if the block of code is successfully completed,
    # the changes are committed to the database.
    # If there is an exception, the changes are rolled back."
    # (c) django documentation
    @transaction.atomic
    def create_account(self,
                       company_name,
                       username,
                       password,
                       company_address=None):
        """Creates a company along with the User and returns them both"""

        company = Company(
            name=company_name,
            address=company_address,
        )

        company.save()

        user = User.objects.create_user(
            username=username,
            password=password,
            company=company,
        )

        return company, user


class Company(models.Model):
    """Global account separator"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('name', max_length=150)
    address = models.CharField('address', max_length=250, blank=True)

    # 'editable=False' won't allow to show this field in admin panel
    # the company with this flag will be set
    # as the default one for every new created
    # user who somehow skipped the Company assignment
    is_default_company = models.BooleanField(default=False, editable=False)

    objects = CompanyManager()

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company,
                                related_name='%(class)s',
                                on_delete=models.CASCADE,
                                null=True,
                                editable=False,
                                )

    class Meta:
        db_table = 'users'

    def __str__(self):
        # check if user has a company assigned
        if self.company\
                and hasattr(self.company, 'name'):
            return f'({self.company.name}) - {self.username}'
        else:
            return f'(null) - {self.username}'

