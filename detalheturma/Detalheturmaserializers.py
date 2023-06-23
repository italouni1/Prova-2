from rest_framework import serializers
from .models import DetalheTurma
class Detalheturmaserializer(serializers.ModelSerializer):

    class Meta:

        model = DetalheTurma
    
        fields = [
            'Codigoprofessor','Codigoaluno','CodigoTurma']