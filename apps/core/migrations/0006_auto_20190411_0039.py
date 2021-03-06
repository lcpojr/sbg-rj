# Generated by Django 2.2 on 2019-04-11 00:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_gallery_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='apresentation',
            field=models.FileField(upload_to='events/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'ppt', 'pptx'], 'Formato de apresentação inválido (.pdf, .ppt, .pptx)')], verbose_name='Apresentação'),
        ),
        migrations.AlterField(
            model_name='event',
            name='icon',
            field=models.ImageField(upload_to='events/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], 'Formato de ícone inválido (.png, .jpg, jpeg)')], verbose_name='Ícone'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='events/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], 'Formato de imagem inválido (.png, .jpg, jpeg)')], verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='news',
            name='icon',
            field=models.ImageField(upload_to='news/%Y-%m-%d', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], 'Formato de imagem inválido (.png, .jpg, .jpeg)')], verbose_name='Ícone'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/%Y-%m-%d', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], 'Formato de imagem inválido (.png, .jpg, .jpeg)')], verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='products/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], 'Formato de imagem inválido (.png, .jpg, jpeg)')], verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(upload_to='products/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], 'Formato de ícone inválido (.png, .jpg, jpeg)')], verbose_name='Ícone'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], 'Formato de imagem inválido (.png, .jpg, jpeg)')], verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='document',
            field=models.FileField(upload_to='publications/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Formato de publicação inválido (.pdf)')], verbose_name='Documento'),
        ),
    ]
