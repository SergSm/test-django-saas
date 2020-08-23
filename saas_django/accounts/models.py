import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models, transaction

DEFAULT_NON_EXISTENT_COMPANY_NAME = 'non existent company'


# top level function
def get_default_company():
    """get or create the non existent company for new users"""

    # NOTE: trying to make this function as the 'User' class @static/class method
    # leads to impossibility to makemigrations
    # The error will be:
    #   ValueError: Cannot serialize: <classmethod object at 0x00000124A17AC940>
    #   There are some values Django cannot serialize into migration files.

    return Company.objects.get_or_create(is_default_company=True,
                                         name=DEFAULT_NON_EXISTENT_COMPANY_NAME)[0].pk


class CompanyManager(models.Manager):
    """Manager for the Company model. Also handles the account creation
    Provides user creation only with the company"""

    # "if the block of code is successfully completed,
    # the changes are committed to the database.
    # If there is an exception, the changes are rolled back." (c) django documentation
    @transaction.atomic
    def create_account(self, company_name, username, password, company_address=None):
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
    # the company with this flag will be set as the default one for every new created
    # user who somehow skipped the Company assignment
    is_default_company = models.BooleanField(default=False, editable=False)

    objects = CompanyManager()

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name


class User(AbstractUser):



    #def get_default_company(cls):
    # @classmethod
    # @staticmethod
    # def get_default_company():
    #     """get or create the non existent company for new users"""
    #     return Company.objects.get_or_create(is_default_company=True,
    #                                          name=DEFAULT_NON_EXISTENT_COMPANY_NAME)[0]
        #return Company.objects.first().pk

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company,
                                related_name='%(class)s',
                                on_delete=models.CASCADE,
                                editable=False,
                                default=get_default_company)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'({self.company.name}) - {self.username}'


#
#   File "D:\rep\test-a
#   ccounts-projects\venv\lib\site-packages\django\db\backends\sqlite3\base.py", line 380, in check_constraints
#     bad_row[1], referenced_table_name, referenced_column_name,
# django.db.utils.IntegrityError: The row in table 'users' with primary key '9e6f6f46464a4a08b156b1c61db76aed' has an invalid foreign key: users.company_id contains a value '0000000
# 000000000000002215e7bb6c6' that does not have a corresponding value in companies.id.

