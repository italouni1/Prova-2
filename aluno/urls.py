from django.urls import path, include
from rest_framework import routers
from .views import AlunoViewSets

router = routers.DefaultRouter()
router.register(r'Aluno', AlunoViewSets)
urlpatterns = [
    path('', include(router.urls)),
]