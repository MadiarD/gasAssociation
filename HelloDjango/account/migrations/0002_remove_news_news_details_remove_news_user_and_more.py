# Generated by Django 5.0.3 on 2024-05-05 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_details',
        ),
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
        migrations.DeleteModel(
            name='NewsSubscribeList',
        ),
        migrations.DeleteModel(
            name='NewsDetails',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
