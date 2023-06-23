from rest_framework import viewsets
from .models import Turma
from .Turmasserializers import Turmaserializer

class TurmaViewSets(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = Turmaserializer