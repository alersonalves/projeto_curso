from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='inicio'),
     path('outro', views.novo, name='novo'),

    # Alunos
     path('listar_alunos', views.listarAluno,
          name='listar_aluno'),
     path('incluir_aluno', views.incluirAluno,
          name='incluir_aluno'),
     path('editar_aluno/<int:id>', views.editarAluno,
          name='editar_aluno'),
     path('excluir_aluno/<int:id>', views.excluirAluno,
          name='excluir_aluno'),

     # Curso
     path('listar_cursos', views.listarCurso,
          name='listar_curso'),
     path('incluir_curso', views.incluirCurso,
          name='incluir_curso'),
     path('editar_curso/<int:id>', views.editarCurso,
          name='editar_curso'),
     path('excluir_curso/<int:id>', views.excluirCurso,
          name='excluir_curso'),
     
]