# Generated by Django 3.0.8 on 2020-07-24 06:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tumblr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tumblr_name', models.CharField(default='', max_length=70)),
                ('json_response', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
