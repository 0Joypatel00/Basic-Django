# Generated by Django 4.0.3 on 2022-04-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='small_des',
            field=models.TextField(blank=True),
        ),
    ]
