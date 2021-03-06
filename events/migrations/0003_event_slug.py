# Generated by Django 3.0.2 on 2020-01-18 04:24

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200118_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=events.models.generate_id, max_length=25, unique=True),
        ),
    ]
