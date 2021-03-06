# Generated by Django 2.2 on 2019-04-07 15:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário responsável pela criação do registro (notícia).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_creator_set', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_by',
            field=models.ForeignKey(blank=True, help_text='Usuário responsável pela ultima atualização do registro (notícia).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_updater_set', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador'),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('category', models.CharField(max_length=50, null=True, verbose_name='Categoria')),
                ('document', models.FileField(upload_to='media/publications/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Formato de publicação inválido (.pdf)')], verbose_name='Documento')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima atualização')),
                ('created_by', models.ForeignKey(blank=True, help_text='Usuário responsável pela criação do registro (publicação).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publication_creator_set', to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
                ('updated_by', models.ForeignKey(blank=True, help_text='Usuário responsável pela ultima atualização do registro (publicação).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publication_updater_set', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador')),
            ],
            options={
                'verbose_name': 'Publicação',
                'verbose_name_plural': 'Publicações',
            },
        ),
    ]
