# Generated by Django 5.1.2 on 2024-10-17 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0003_apply_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_job',
            name='job_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]