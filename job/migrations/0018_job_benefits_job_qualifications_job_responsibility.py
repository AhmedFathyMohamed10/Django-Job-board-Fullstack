# Generated by Django 5.0.4 on 2024-04-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_job_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='benefits',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='job',
            name='qualifications',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='job',
            name='responsibility',
            field=models.TextField(default=''),
        ),
    ]
