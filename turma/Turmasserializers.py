from rest_framework import serializers
from .models import Turma
class Turmaserializer(serializers.ModelSerializer):

    class Meta:

        model = Turma
    
        fields = [
            'codigo','codigocurso']