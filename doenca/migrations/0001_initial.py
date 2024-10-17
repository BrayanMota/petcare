# Generated by Django 4.2.13 on 2024-10-17 17:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('sinais_clinicos', models.TextField()),
                ('transmissao', models.TextField()),
                ('tratamentos', models.TextField()),
            ],
            options={
                'verbose_name': 'Doença',
                'verbose_name_plural': 'Doenças',
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('testes', models.TextField()),
                ('doenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnostico', to='doenca.doenca')),
            ],
            options={
                'verbose_name': 'Diagnóstico',
                'verbose_name_plural': 'Diagnósticos',
            },
        ),
        migrations.CreateModel(
            name='Apresentacao',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('ordem', models.PositiveIntegerField()),
                ('tipo_conteudo', models.CharField(choices=[('TEXTO', 'Texto'), ('IMAGEM', 'Imagem')], max_length=10)),
                ('conteudo_texto', models.TextField(blank=True, null=True)),
                ('conteudo_imagem', models.ImageField(blank=True, null=True, upload_to='disease_images/')),
                ('doenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apresentacao', to='doenca.doenca')),
            ],
            options={
                'verbose_name': 'Apresentação',
                'verbose_name_plural': 'Apresentações',
                'ordering': ['ordem'],
            },
        ),
    ]
