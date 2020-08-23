# Generated by Django 3.1 on 2020-08-23 10:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200823_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b7a5479a-4fa6-4288-9c44-ea670cc48555'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
    ]
