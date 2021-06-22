from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=70, null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF", unique=True)
    telefone = models.CharField(max_length=16, null=True, unique=True)

    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
