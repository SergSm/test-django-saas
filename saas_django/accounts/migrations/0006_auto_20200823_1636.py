# Generated by Django 3.1 on 2020-08-23 10:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200823_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b12cbe94-e26c-437c-98eb-bc89b192167a'), editable=False, primary_key=True, serialize=False),
        ),
    ]