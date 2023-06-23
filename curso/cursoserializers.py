from rest_framework import serializers
from .models import Curso
class Cursoserializer(serializers.ModelSerializer):

    class Meta:

        model = Curso
    
        fields = [
            'codigo','nome']