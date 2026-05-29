from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import PlanoAlimentar
from .serializers import PlanoAlimentarSerializer 
from .forms import PlanoAlimentarForm

class PlanoAlimentarViewSet(viewsets.ModelViewSet):
    queryset = PlanoAlimentar.objects.all()
    serializer_class = PlanoAlimentarSerializer

def add_planoalimentar(request):
    template_name = 'planosalimentares/add_planoalimentar.html'
    context = {}
    if request.method == 'POST':
        form = PlanoAlimentarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planosalimentares:list_planosalimentares')
    else:
        form = PlanoAlimentarForm()
    context['form'] = form
    return render(request, template_name, context)

def list_planosalimentares(request):
    template_name = 'planosalimentares/list_planosalimentares.html'
    planos = PlanoAlimentar.objects.all()
    context = {
        'planos': planos,
    }
    return render(request, template_name, context)

def edit_planoalimentar(request, id_plano):
    template_name = 'planosalimentares/add_planoalimentar.html'
    context = {}
    plano = get_object_or_404(PlanoAlimentar, id=id_plano)
    
    if request.method == 'POST':
        form = PlanoAlimentarForm(request.POST, instance=plano)
        if form.is_valid():
            form.save()
            return redirect('planosalimentares:list_planosalimentares')
    else:
        form = PlanoAlimentarForm(instance=plano)
        
    context['form'] = form
    return render(request, template_name, context)

def delete_planoalimentar(request, id_plano):
    plano = get_object_or_404(PlanoAlimentar, id=id_plano)
    plano.delete()
    return redirect('planosalimentares:list_planosalimentares')