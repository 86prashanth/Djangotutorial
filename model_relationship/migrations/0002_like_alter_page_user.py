# Generated by Django 4.2.4 on 2023-08-29 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('model_relationship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('pen', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='model_relationship.page')),
                ('likes', models.IntegerField()),
            ],
            bases=('model_relationship.page',),
        ),
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
