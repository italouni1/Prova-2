from rest_framework import viewsets
from .models import Disciplina
from .Disciplinaserializers import DisciplinaSerializer

class DisciplinaViewSets(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer