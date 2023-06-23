from django.urls import path, include
from rest_framework import routers
from .views import TurmaViewSets

router = routers.DefaultRouter()
router.register(r'turma', TurmaViewSets)

urlpatterns = [
    path('', include(router.urls)),
]