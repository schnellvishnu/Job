# Generated by Django 5.1.2 on 2024-10-23 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0007_apply_job_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply_job',
            name='photo',
        ),
    ]