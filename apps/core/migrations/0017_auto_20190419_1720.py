# Generated by Django 2.2 on 2019-04-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20190417_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('AS', 'Anais de Simpósio'), ('AC', 'Anais de Congresso'), ('CLIP', 'Clippings')], max_length=50, null=True, verbose_name='Categoria'),
        ),
    ]
