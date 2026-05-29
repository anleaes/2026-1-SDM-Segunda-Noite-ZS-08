from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

# Importações dos seus models
from .models import Treino
from itemtreino.models import ItemTreino
from exercicios.models import Exercicio
from alunos.models import Aluno
from instrutores.models import Instrutor

from .serializers import TreinoSerializer 
from .forms import TreinoForm

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer

def add_treino(request):
    template_name = 'treinos/add_treino.html'
    context = {}
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treinos:list_treinos')
    else:
        form = TreinoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_treinos(request):
    template_name = 'treinos/list_treinos.html'
    treinos = Treino.objects.all()
    context = {
        'treinos': treinos,
    }
    return render(request, template_name, context)

def edit_treino(request, id_treino):
    template_name = 'treinos/add_treino.html'
    context = {}
    treino = get_object_or_404(Treino, id=id_treino)
    
    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('treinos:list_treinos')
    else:
        form = TreinoForm(instance=treino)
        
    context['form'] = form
    return render(request, template_name, context)

def delete_treino(request, id_treino):
    treino = get_object_or_404(Treino, id=id_treino)
    treino.delete()
    return redirect('treinos:list_treinos')

def list_exercicios_add(request):
    template_name = 'treinos/list_exercicios_add.html'
    exercicios = Exercicio.objects.all()
    context = {
        'exercicios': exercicios,
    }
    return render(request, template_name, context)

def montar_treino(request):
    template_name = 'treinos/montar_treino.html'
    cart = request.session.get('treino_cart', {})
    context = {
        'cart': cart,
    }
    return render(request, template_name, context)

def add_exercicio_treino(request, id_exercicio):
    exercicio = get_object_or_404(Exercicio, id=id_exercicio)
    cart = request.session.get('treino_cart', {})
    pid = str(exercicio.id)
    
    if pid not in cart:
        cart[pid] = {
            'nome': exercicio.nome,
            'series': 3,
            'repeticoes': 10,
            'carga_kg': 0.0,
            'intervalo_segundos': 60,
            'observacoes': ''
        }
        
    request.session['treino_cart'] = cart
    request.session.modified = True
    return redirect('treinos:montar_treino')

def edit_exercicio_treino(request, id_exercicio):
    if request.method == 'POST':
        cart = request.session.get('treino_cart', {})
        pid = str(id_exercicio)
        
        if pid in cart:
            cart[pid]['series'] = int(request.POST.get('series', 3))
            cart[pid]['repeticoes'] = int(request.POST.get('repeticoes', 10))
            cart[pid]['carga_kg'] = float(request.POST.get('carga_kg', 0.0))
            cart[pid]['intervalo_segundos'] = int(request.POST.get('intervalo_segundos', 60))
            cart[pid]['observacoes'] = request.POST.get('observacoes', '')
            
        request.session['treino_cart'] = cart
        request.session.modified = True
    return redirect('treinos:montar_treino')

def delete_exercicio_treino(request, id_exercicio):
    cart = request.session.get('treino_cart', {})
    pid = str(id_exercicio)
    if pid in cart:
        del cart[pid]
    request.session['treino_cart'] = cart
    request.session.modified = True
    return redirect('treinos:montar_treino')

def finalizar_treino(request):
    template_name = 'treinos/finalizar_treino.html'
    cart = request.session.get('treino_cart', {})
    alunos = Aluno.objects.all()
    instrutores = Instrutor.objects.all()

    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        instrutor_id = request.POST.get('instrutor')
        nome_treino = request.POST.get('nome')
        descricao = request.POST.get('descricao', '')
        duracao = request.POST.get('duracao_minutos', 60)

        aluno = get_object_or_404(Aluno, id=aluno_id)
        instrutor = get_object_or_404(Instrutor, id=instrutor_id)

        treino = Treino.objects.create(
            aluno=aluno,
            instrutor=instrutor,
            nome=nome_treino,
            descricao=descricao,
            duracao_minutos=duracao
        )

        for exercicio_id, item in cart.items():
            ex = get_object_or_404(Exercicio, id=exercicio_id)
            ItemTreino.objects.create(
                treino=treino,
                exercicio=ex,
                series=int(item['series']),
                repeticoes=int(item['repeticoes']),
                carga_kg=float(item['carga_kg']),
                intervalo_segundos=int(item['intervalo_segundos']),
                observacoes=item['observacoes']
            )
            
        request.session['treino_cart'] = {}
        request.session.modified = True
        return redirect('treinos:view_treino', id_treino=treino.id)
        
    context = {
        'cart': cart,
        'alunos': alunos,
        'instrutores': instrutores,
    }
    return render(request, template_name, context)

def view_treino(request, id_treino):
    template_name = 'treinos/view_treino.html'
    treino = get_object_or_404(Treino, id=id_treino)
    itens = treino.itens.all()
    context = {
        'treino': treino,
        'itens': itens,
    }
    return render(request, template_name, context)