# Generated by Django 2.2 on 2019-04-21 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_slideshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='resume',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, verbose_name='Resumo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
