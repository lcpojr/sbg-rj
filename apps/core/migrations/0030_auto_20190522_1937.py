# Generated by Django 2.2 on 2019-05-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20190522_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='link_to_gallery',
            field=models.URLField(blank=True, null=True, verbose_name='Link para a Galeria Completa'),
        ),
    ]