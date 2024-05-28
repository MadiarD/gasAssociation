# Generated by Django 5.0.3 on 2024-05-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
