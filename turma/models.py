from django.db import models

class Turma(models.Model):

  Codigo = models.CharField(max_length=100)
  Codigocurso= models.CharField(max_length=100)