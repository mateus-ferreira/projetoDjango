from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
app_name = "biblioteca"

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', include('blog.urls', namespace="blog")),
    path('cadastrarAluno', views.cadastrarAluno, name='cadastrarAluno'),
    path('cadastrarLivro', views.cadastrarLivro, name='cadastrarLivro'),
    path('cadastrarEmprestimo', views.cadastrarEmprestimo, name='cadastrarEmprestimo'),
    path('exibirAlunos', views.exibirAlunos, name='exibirAlunos'),
    path('exibirLivros', views.exibirLivros, name='exibirLivros'),
    path('exibirEmprestimos', views.exibirEmprestimos, name='exibirEmprestimos'),
]
