# Generated by Django 5.1.1 on 2025-04-02 08:20

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'رخداد', 'verbose_name_plural': 'رخدادها'},
        ),
        migrations.AddField(
            model_name='event',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='event',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='capacity',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='ظرفیت رخداد'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='سالن همایش قاسم سلیمانی', max_length=200, verbose_name='مکان برگزاری'),
        ),
        migrations.AlterField(
            model_name='event',
            name='schedule_date',
            field=django_jalali.db.models.jDateTimeField(verbose_name='تاریخ برگزاری'),
        ),
    ]
