from django.db import models
from django.contrib.auth.models import User


class Campo(models.Model):
    nome = models.CharField('Nome', max_length=40)
    descricao = models.TextField('Descrição', null=True, blank=True)


    def __str__(self):
        return self.nome


class Atividade(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT, verbose_name="Matéria")
    numero = models.IntegerField('Número', )
    descricao = models.TextField('Descrição', null=True, blank=True)
    pontos = models.DecimalField(max_digits=4, decimal_places=1)
    detalhes = models.CharField(max_length=100)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return f'Atividade {self.numero} - {self.campo.nome}'
