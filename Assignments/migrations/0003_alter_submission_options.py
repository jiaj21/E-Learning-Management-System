# Generated by Django 4.2.1 on 2023-05-28 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assignments', '0002_remove_assignments_id_assignments_assign_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'verbose_name_plural': 'Submission'},
        ),
    ]
