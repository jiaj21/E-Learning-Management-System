# Generated by Django 4.2.1 on 2023-05-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignments', '0003_alter_submission_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='assign_file',
            field=models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='question/'),
        ),
    ]
