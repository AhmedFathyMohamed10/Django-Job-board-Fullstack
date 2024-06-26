# Generated by Django 5.0.4 on 2024-04-28 10:30

import job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.helper_upload_image),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
