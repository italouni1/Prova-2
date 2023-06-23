from rest_framework import viewsets
from .models import Professor
from .Professorserializers import ProfessorSerializer

class ProfessorViewSets(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer