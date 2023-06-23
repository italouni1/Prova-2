from django.db import models

class Detalhecurso(models.Model):

  CodigoCurso= models.CharField(max_length=100)
  CodigoTurma= models.CharField(max_length=100)
  