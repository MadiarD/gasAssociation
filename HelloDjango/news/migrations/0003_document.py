# Generated by Django 5.0.3 on 2024-05-14 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_memberdetail_price_per_m3'),
        ('news', '0002_alter_newsdetails_img'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('notification', 'Хабарландыру'), ('contract', 'Келісімшарт'), ('report', 'Есеп'), ('instruction', 'Нұсқаулық')], max_length=100)),
                ('file', models.FileField(upload_to='documents/')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_document', to='members.members')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_document', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
