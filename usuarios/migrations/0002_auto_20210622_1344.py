# Generated by Django 3.2.4 on 2021-06-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nome_completo',
            field=models.CharField(max_length=70, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
