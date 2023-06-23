from rest_framework import viewsets
from .models import Curso
from .cursoserializers import Cursoserializer

class CursoViewSets(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = Cursoserializer