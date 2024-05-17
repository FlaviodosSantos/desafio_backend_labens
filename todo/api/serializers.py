from rest_framework import serializers
from todo import models


class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tarefas
        fields = '__all__'