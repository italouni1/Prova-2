from rest_framework import viewsets
from .models import DetalheTurma
from .Detalheturmaserializers import Detalheturmaserializer

class DetalheTurmaViewSets(viewsets.ModelViewSet):
    queryset = DetalheTurma.objects.all()
    serializer_class = Detalheturmaserializer
