# Generated by Django 2.2 on 2019-04-23 16:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20190423_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='news',
            name='resume',
            field=tinymce.models.HTMLField(verbose_name='Resumo da Notícia'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Descrição'),
        ),
    ]