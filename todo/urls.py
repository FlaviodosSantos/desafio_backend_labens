from django.urls import include, path
from rest_framework import routers

from todo.api.viewsets import TarefasViewSet

router = routers.DefaultRouter()
router.register(r'', TarefasViewSet, basename='Tarefas')

urlpatterns = [
    path('', include(router.urls)),
]