from django.urls import path, include
from rest_framework import routers
from .views import ProfessorViewSets

router = routers.DefaultRouter()
router.register(r'professores', ProfessorViewSets)

urlpatterns = [
    path('', include(router.urls)),
]