# Generated by Django 5.0.3 on 2024-05-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_receipt_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
