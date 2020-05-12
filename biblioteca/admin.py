from django.contrib import admin
from .models import Livro, Aluno, Emprestimo

admin.site.register(Livro)
admin.site.register(Aluno)
admin.site.register(Emprestimo)