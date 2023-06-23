from rest_framework import serializers
from .models import Aluno
class Alunoserializer(serializers.ModelSerializer):

    class Meta:

        model = Aluno
    
        fields = [
            'nome','sexo','matricula','datanascimento']