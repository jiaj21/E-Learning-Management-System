# Generated by Django 4.2.1 on 2023-05-23 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('studentKey', models.IntegerField(unique=True)),
                ('facultyKey', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stud_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email_id', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('course_name', models.ManyToManyField(blank=True, related_name='students', to='main.course')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='main.department')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('fac_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty', to='main.department')),
            ],
            options={
                'verbose_name_plural': 'Faculty',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='main.department'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.faculty'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('course_code', 'department_name', 'course_name')},
        ),
    ]
