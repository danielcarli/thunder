# Generated by Django 4.2.1 on 2023-05-21 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0013_remove_task_milestone_remove_task_users_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('deadline_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('assigned', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('commmunication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.communicationdemand')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('description', models.TextField()),
                ('deadline_date', models.DateTimeField(null=True)),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.milestone')),
            ],
        ),
        migrations.CreateModel(
            name='UserTaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('status', models.CharField(choices=[('CANCELED', 'Canceled'), ('TO DO', 'To do'), ('DOING', 'Doing'), ('DONE', 'Done')], default='TO DO', max_length=20)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(through='campaigns.UserTaskStatus', to=settings.AUTH_USER_MODEL),
        ),
    ]
