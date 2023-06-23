from rest_framework import viewsets
from .models import Detalhecurso
from .Detalhecursoserializers import Detalhecursoserializer

class DetalhecursoViewSets(viewsets.ModelViewSet):
    queryset = Detalhecurso.objects.all()
    serializer_class = Detalhecursoserializer