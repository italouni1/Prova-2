from rest_framework import viewsets
from .models import Aluno
from .alunoserializers import Alunoserializer

class AlunoViewSets(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = Alunoserializer