# Generated by Django 5.1.1 on 2024-10-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_eventuser_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='سالن همایش قاسم سلیمانی', max_length=200, verbose_name='location'),
        ),
    ]