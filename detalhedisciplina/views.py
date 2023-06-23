from rest_framework import viewsets
from .models import Detalhedisciplina
from .Detalhedisciplinaserializers import DetalheDisciplinaserializer

class DetalhedisciplinaViewSets(viewsets.ModelViewSet):
    queryset = Detalhedisciplina.objects.all()
    serializer_class = DetalheDisciplinaserializer

