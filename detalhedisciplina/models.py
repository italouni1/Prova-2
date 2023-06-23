from django.db import models

class Detalhedisciplina(models.Model):

  codigocurso = models.CharField(max_length=100)
  codigocdisciplina= models.CharField(max_length=100)
  