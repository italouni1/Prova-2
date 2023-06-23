from rest_framework import serializers
from .models import Detalhedisciplina
class DetalheDisciplinaserializer(serializers.ModelSerializer):

    class Meta:

        model = Detalhedisciplina
        fields = [
            'codigo curso','codigo disciplina']