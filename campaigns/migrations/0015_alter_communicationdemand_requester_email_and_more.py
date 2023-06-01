# Generated by Django 4.2.1 on 2023-05-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0014_milestone_task_usertaskstatus_task_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationdemand',
            name='requester_email',
            field=models.EmailField(default=None, max_length=254, null=True, verbose_name='E-mail do solicitante'),
        ),
        migrations.AlterField(
            model_name='communicationdemand',
            name='requester_whatsapp',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='Whatsapp do solicitante'),
        ),
    ]
