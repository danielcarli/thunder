# Generated by Django 4.2.1 on 2023-05-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Campain creation date')),
                ('final_deadline', models.DateTimeField(verbose_name='Final Campaign deadline')),
                ('general_drive_url', models.URLField()),
                ('deliverables_drive_url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]
