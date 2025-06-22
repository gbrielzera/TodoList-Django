from django.shortcuts import get_object_or_404, render, redirect
from .models import TodoList
from django.contrib import messages

# Create your views here.


def home(request):
    items = TodoList.objects.all()
    return render(request, "home.html", {"todos": items})


def criar_tarefa(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            TodoList.objects.create(title=title)
    return redirect('home')


def atualizar_tarefa(request, id):
    tarefa = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        if 'completed' in request.POST:
            tarefa.isCompleted = True
        else:
            tarefa.isCompleted = False
        tarefa.save()
    return redirect('home')

def deletar_tarefa(request, id):
    tarefa = TodoList.objects.get(id=id)
    tarefa.delete()
    return redirect('home')

def editar_tarefa(request, id):
    todo = get_object_or_404(TodoList, id=id)
    
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.isCompleted = 'isCompleted' in request.POST
        todo.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('home')  # Ajuste o nome da url home se for diferente
    
    # Se quiser tratar GET (não usado nesse modal), pode retornar algo aqui ou redirecionar
    return redirect('home')

