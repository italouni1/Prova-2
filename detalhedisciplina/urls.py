from django.urls import path, include
from rest_framework import routers
from .views import DetalhedisciplinaViewSets

router = routers.DefaultRouter()
router.register(r'detalhe disciplina', DetalhedisciplinaViewSets)
urlpatterns = [
    path('', include(router.urls)),
]