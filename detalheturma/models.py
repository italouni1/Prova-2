from django.db import models

class DetalheTurma(models.Model):

  CodigoAluno = models.CharField(max_length=100)
  CodigoProfessor= models.CharField(max_length=100)
  CodigoTurma = models.CharField(max_length=100)