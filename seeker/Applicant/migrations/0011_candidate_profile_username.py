# Generated by Django 5.1.2 on 2024-10-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0010_apply_job_description_apply_job_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_profile',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]