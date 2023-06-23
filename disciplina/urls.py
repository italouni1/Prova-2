from django.urls import path, include
from rest_framework import routers
from .views import DisciplinaViewSets

router = routers.DefaultRouter()
router.register(r'disciplinas', DisciplinaViewSets)

urlpatterns = [
    path('', include(router.urls)),
]