# Generated by Django 4.2.4 on 2023-08-29 18:01

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proxystudent',
            fields=[
            ],
            options={
                'ordering': ['name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('manager_app.manager_student',),
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
    ]
