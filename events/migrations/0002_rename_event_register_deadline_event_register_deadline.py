# Generated by Django 5.1.1 on 2024-10-12 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_register_deadline',
            new_name='register_deadline',
        ),
    ]
