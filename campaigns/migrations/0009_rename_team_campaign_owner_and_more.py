# Generated by Django 4.2.1 on 2023-05-20 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0008_alter_campaign_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='team',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='team',
            new_name='assigned',
        ),
    ]
