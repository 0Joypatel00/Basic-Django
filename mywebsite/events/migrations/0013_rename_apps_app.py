# Generated by Django 4.0.3 on 2022-04-12 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_apps'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apps',
            new_name='App',
        ),
    ]