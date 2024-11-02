# Generated by Django 5.1.2 on 2024-10-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0002_rename_compnay_profile_candidate_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job_code', models.CharField(max_length=100, null=True, unique=True)),
                ('candidate_name', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(max_length=100, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('expect_salary', models.CharField(max_length=100, null=True)),
                ('current_salary', models.CharField(max_length=100, null=True)),
                ('cv_file', models.FileField(null=True, upload_to='')),
                ('status', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
