# Generated by Django 4.2.1 on 2023-05-21 03:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0019_alter_communicationtype_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='communicationdemand',
            name='managers',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
