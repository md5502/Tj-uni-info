# Generated by Django 5.1.1 on 2024-10-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahid', '0002_remove_shahid_description_shahid_life_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='shahid',
            name='profile_image',
            field=models.ImageField(default='shohada/profiles/default.svg', upload_to='shohada/profiles', verbose_name='عکس پروفایل'),
        ),
    ]
