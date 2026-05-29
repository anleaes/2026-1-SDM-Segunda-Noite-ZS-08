from django.shortcuts import render, get_object_or_404, redirect
from .models import PlanosMensalidade
from rest_framework import viewsets
from .serializer import PlanosMensalidadeSerializer
from .forms import PlanosMensalidadeForm

# Create your views here.
class PlanosMensalidadeViewSet(viewsets.ModelViewSet):
    queryset = PlanosMensalidade.objects.all()
    serializer_class = PlanosMensalidadeSerializer

def add_plano(request):
    template_name = 'planosmensalidade/add_plano.html'
    context = {}
    if request.method == 'POST':
        form = PlanosMensalidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planosmensalidade:list_planos')
    form = PlanosMensalidadeForm()
    context['form'] = form
    return render(request, template_name, context)

def list_planos(request):
    template_name = 'planosmensalidade/list_planos.html'
    planos = PlanosMensalidade.objects.all()
    context = {
        'planos': planos,
    }
    return render(request, template_name, context)

def edit_plano(request, id_plano):
    template_name = 'planosmensalidade/add_plano.html'
    context = {}
    plano = get_object_or_404(PlanosMensalidade, id=id_plano)
    if request.method == 'POST':
        form = PlanosMensalidadeForm(request.POST, instance=plano)
        if form.is_valid():
            form.save()
            return redirect('planosmensalidade:list_planos')
    form = PlanosMensalidadeForm(instance=plano)
    context['form'] = form
    return render(request, template_name, context)

def delete_plano(request, id_plano):
    plano = PlanosMensalidade.objects.get(id=id_plano)
    plano.delete()
    return redirect('planosmensalidade:list_planos')