# Generated by Django 5.1.1 on 2024-10-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0002_association_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='association',
            options={'verbose_name': 'انجمن', 'verbose_name_plural': 'انجمن ها'},
        ),
        migrations.AlterModelOptions(
            name='associationuser',
            options={'verbose_name': 'عضو انجمن', 'verbose_name_plural': 'اعضای انجمن'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'عضو', 'verbose_name_plural': 'اعضا'},
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='شناسه'),
        ),
    ]
