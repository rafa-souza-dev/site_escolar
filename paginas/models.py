from django.db import models
from django.contrib.auth.models import User


def user_path(instance, filename):
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


class Campo(models.Model):
    nome = models.CharField('Nome', max_length=40)
    descricao = models.TextField('Descrição', null=True, blank=True)


    def __str__(self):
        return self.nome


class Atividade(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    numero = models.IntegerField('Número', )
    descricao = models.TextField('Descrição', null=True, blank=True)
    pontos = models.DecimalField(max_digits=4, decimal_places=1)
    detalhes = models.CharField(max_length=100)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return f'Atividade {self.numero} - {self.campo.nome}'


class Comprovante(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()
    data_final = models.DateField(null=True, blank=True, help_text="Informar apenas se o comprovante for relativo "
                                                                   " a um período.")
    arquivo = models.FileField(upload_to=user_path)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return f'{self.atividade} - ({self.quantidade})'


class Progressao(models.Model):
    data = models.DateField()
    data_final = models.DateField(null=True, blank=True, help_text="Informar apenas se"
                                                                   "o comprovante for relativo a um período.")
    observacao = models.TextField('Observação')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
