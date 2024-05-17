from django.db import models


SITUACAO = [("nova","Nova"), ("em_andamento","Em andamento"), ("concluida","Concluída"), ("cancelada","Cancelada")]

class Tarefas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    prazo = models.DateField()
    data_conclusao = models.DateField()
    situacao = models.CharField(choices=SITUACAO, max_length=13)
