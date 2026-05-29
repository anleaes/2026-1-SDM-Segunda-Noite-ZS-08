from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Treino
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