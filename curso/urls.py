from django.urls import path, include
from rest_framework import routers
from .views import CursoViewSets

router = routers.DefaultRouter()
router.register(r'Curso', CursoViewSets)

urlpatterns = [
    path('', include(router.urls)),
]