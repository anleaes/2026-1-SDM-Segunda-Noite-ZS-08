from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Alimento
from .serializers import AlimentoSerializer
from .forms import AlimentoForm

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

def add_alimento(request):
    template_name = 'alimentos/add_alimento.html'
    context = {}
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alimentos:list_alimentos')
    form = AlimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_alimentos(request):
    template_name = 'alimentos/list_alimentos.html'
    alimentos = Alimento.objects.all()
    context = {
        'alimentos': alimentos,
    }
    return render(request, template_name, context)

def edit_alimento(request, id_alimento):
    template_name = 'alimentos/add_alimento.html'
    context = {}
    alimento = get_object_or_404(Alimento, id=id_alimento)
    
    if request.method == 'POST':
        form = AlimentoForm(request.POST, instance=alimento)
        if form.is_valid():
            form.save()
            return redirect('alimentos:list_alimentos')
    else:
        form = AlimentoForm(instance=alimento)
        
    context['form'] = form
    return render(request, template_name, context)

def delete_alimento(request, id_alimento):
    alimento = Alimento.objects.get(id=id_alimento)
    alimento.delete()
    return redirect('alimentos:list_alimentos')