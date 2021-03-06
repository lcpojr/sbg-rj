# Generated by Django 2.2 on 2019-05-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20190514_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='link_to_gallery',
            field=models.URLField(null=True, verbose_name='Link para a Galeria Completa'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('AS', 'Anais de Simpósio'), ('AC', 'Anais de Congresso'), ('CLIP', 'Clippings'), ('OT', 'Outros')], max_length=50, null=True, verbose_name='Categoria'),
        ),
    ]
