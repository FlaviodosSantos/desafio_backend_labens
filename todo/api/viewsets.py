from rest_framework import viewsets
from todo.api.serializers import TarefasSerializer
from todo.models import Tarefas


class TarefasViewSet(viewsets.ModelViewSet):
    serializer_class = TarefasSerializer
    queryset = Tarefas.objects.all()