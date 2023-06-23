from django.urls import re_path as url, include
from django.contrib import admin

urlpatterns = [
    url(r'^professor/', include('professor.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^disciplina/', include('disciplina.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^turma/', include('turma.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^aluno/', include('aluno.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^detalhedisciplina/', include('detalhedisciplina.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^detalheturma/', include('detalheturma.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^detalhecurso/', include('detalhecurso.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^curso/', include('curso.urls')),
    url(r'^admin/', admin.site.urls),
]

