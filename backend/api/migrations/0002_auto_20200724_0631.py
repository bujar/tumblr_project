# Generated by Django 3.0.8 on 2020-07-24 06:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TumblrCache',
            fields=[
                ('tumblr_name', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('json_response', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tumblr',
        ),
    ]
