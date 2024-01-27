from django.shortcuts import render, redirect
from django.http import HttpResponse
from teste.forms import AlunoForm, CursoForm
from teste.models import Aluno, Curso

# Create your views here.

def index(request):
    return render(request, 'inicio.html')

def novo(request):
    return HttpResponse("Esta é uma página de teste")

# Alunos

def listarAluno(request):
    busca = request.GET.get('busca')
    ordem = request.GET.get('ordem')
    if busca:
        if not ordem or ordem == 'nome':
            alunos = Aluno.objects.filter(nome__icontains=busca).extra(select={'novo': 'lower(nome)'}).order_by('novo')

        elif ordem == '-nome':
            alunos = Aluno.objects.filter(nome__icontains=busca).extra(select={'novo': 'lower(nome)'}).order_by('-novo')
    else:
        busca = ''
        if not ordem or ordem == 'nome':
            alunos = Aluno.objects.all().extra(select={'novo': 'lower(nome)'}).order_by('novo')

        elif ordem == '-nome':
            alunos = Aluno.objects.all().extra(select={'novo': 'lower(nome)'}).order_by('-novo')

    return render(request, 'listar_aluno.html',
                  {'alunos':alunos, 'busca':busca})

def incluirAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    else:
        form = AlunoForm()
    return render(request, 'incluir_aluno.html',
                  {'form':form})

def editarAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    return render(request, 'incluir_aluno.html',
                  {'form':form})

def excluirAluno(request, id):
    aluno= Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('listar_aluno')

# Cursos

def listarCurso(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, 'listar_curso.html',
                  {'cursos':cursos})

def incluirCurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_curso')
    else:
        form = CursoForm()
    return render(request, 'incluir_curso.html',
                  {'form':form})

def editarCurso(request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(instance=curso)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_curso')
    return render(request, 'incluir_curso.html',
                  {'form':form})

def excluirCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('listar_curso')

