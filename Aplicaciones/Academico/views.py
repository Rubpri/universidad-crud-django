from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.


def home(request):
    cursosListados = Curso.objects.all()
    cantidad_cursos = len(cursosListados)
    return render(request, "gestionCursos.html", {"cursos": cursosListados, "cantidad_cursos": cantidad_cursos})


def registrarCurso(request):

    cursosListados = Curso.objects.all()
    limite_cursos = 10

    if len(cursosListados) < limite_cursos:
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']

        if Curso.objects.filter(codigo=codigo).exists():
            messages.error(request, f'El código {codigo} ya está en uso. Por favor, elige otro código.')
            return redirect('/')
        else:
            curso = Curso.objects.create(
                codigo=codigo, nombre=nombre, creditos=creditos)

            messages.success(request, f'¡{codigo} {nombre} añadido!')
            return redirect('/')

    else:
        messages.error(request, '¡Has alcanzado el número máximo de cursos!')
        return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)

    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, f'¡{codigo} editado!')

    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, f'¡{codigo} eliminado!')

    return redirect('/')
