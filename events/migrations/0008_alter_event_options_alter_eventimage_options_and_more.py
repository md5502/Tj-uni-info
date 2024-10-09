# Generated by Django 5.1.1 on 2024-10-09 05:49

import django.db.models.deletion
import mdeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_event_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'رخداد', 'verbose_name_plural': 'رخداد ها'},
        ),
        migrations.AlterModelOptions(
            name='eventimage',
            options={'verbose_name': 'عکس رخداد', 'verbose_name_plural': 'عکس های رخداد'},
        ),
        migrations.AlterModelOptions(
            name='eventuser',
            options={'verbose_name': 'شرکت\u200cکننده', 'verbose_name_plural': 'شرکت\u200cکننده ها'},
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=mdeditor.fields.MDTextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='سالن همایش قاسم سلیمانی', max_length=200, verbose_name='مکان برگذاری'),
        ),
        migrations.AlterField(
            model_name='event',
            name='schedule_date',
            field=models.DateTimeField(verbose_name='تاریخ برگذاری'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='شناسه'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='ویرایش شده در'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.event', verbose_name='رخداد'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(upload_to='events_images/', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='آدرس ایمیل'),
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_users', to='events.event', verbose_name='رخداد'),
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='fname',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='eventuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='ویرایش شده در'),
        ),
    ]
