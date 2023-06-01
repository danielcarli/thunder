# Generated by Django 4.2.1 on 2023-05-20 22:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0007_remove_task_team_alter_campaign_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='team',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
