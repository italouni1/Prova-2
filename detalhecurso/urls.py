from django.urls import path, include
from rest_framework import routers
from .views import DetalhecursoViewSets

router = routers.DefaultRouter()
router.register(r'detalhecurso', DetalhecursoViewSets)

urlpatterns = [
    path('', include(router.urls)),
]