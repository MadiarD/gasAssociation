# Generated by Django 5.0.3 on 2024-05-10 12:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_paymentaccount_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentaccount',
            name='number',
            field=models.CharField(default=uuid.uuid4, max_length=20, null=True, unique=True),
        ),
    ]