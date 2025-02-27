# Generated by Django 4.2.13 on 2024-11-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doenca", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doenca",
            name="sinais_clinicos",
        ),
        migrations.RemoveField(
            model_name="doenca",
            name="transmissao",
        ),
        migrations.RemoveField(
            model_name="doenca",
            name="tratamentos",
        ),
        migrations.AddField(
            model_name="apresentacao",
            name="topico",
            field=models.CharField(
                choices=[
                    ("Sinal Clínico", "Sinal Clínico"),
                    ("Diagnostico", "Diagnostico"),
                    ("Prevenção", "Prevenção"),
                    ("Ciclo da Doença", "Ciclo da Doença"),
                    ("Boletim Epidemiológico", "Boletim Epidemiológico"),
                ],
                default=1,
                max_length=30,
            ),
            preserve_default=False,
        ),
    ]
