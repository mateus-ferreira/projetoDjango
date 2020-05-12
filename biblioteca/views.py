from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Aluno, Livro, Emprestimo
from .forms import AlunoForm

def index(request):
    return render(request, 'biblioteca/index.html', {})

def cadastrarAluno(request):
	if request.method == "POST":
		aluno = AlunoForm(request.POST)
		if aluno.is_valid():
			alunoSalvar = aluno.save(commit=False)
			alunoSalvar.save()
			return redirect('index')
	formAluno = AlunoForm()
	return render(request, 'biblioteca/cadastrarAluno.html', {'form':formAluno})