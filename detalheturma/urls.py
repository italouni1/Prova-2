from django.urls import path, include
from rest_framework import routers
from .views import DetalheTurmaViewSets

router = routers.DefaultRouter()
router.register(r'detalhe Turma', DetalheTurmaViewSets)
urlpatterns = [
    path('', include(router.urls)),
]