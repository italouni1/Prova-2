from rest_framework import serializers
from .models import Detalhecurso
class Detalhecursoserializer(serializers.ModelSerializer):

    class Meta:

        model = Detalhecurso
    
        fields = [
            'CodigoCurso','CodigoTurma']