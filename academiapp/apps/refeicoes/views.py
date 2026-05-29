from django.shortcuts import render, get_object_or_404, redirect
from .models import Refeicao
from rest_framework import viewsets
from .serializers import RefeicaoSerializer
from .forms import RefeicaoForm
from .models import Refeicao, Alimento

# Create your views here.
class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer
    
    def add_refeicao(request):
        template_name = 'refeicoes/add_refeicoes.html'
    context = {}
    if request.method == 'POST':
        form = RefeicaoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('refeicoes:list_refeicoes')
    form = RefeicaoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_refeicoes(request):
    template_name = 'refeicoes/list_refeicoes.html'
    refeicoes = Refeicao.objects.prefetch_related('alimento')
    context = {
        'refeicoes': refeicao,
    }
    return render(request, template_name, context)

def edit_refeicoes(request, id_client):
    template_name = 'refeicoes/add_refeicao.html'
    context ={}
    refeicao = get_object_or_404(refeicao, id=id_refeicao)
    if request.method == 'POST':
        form = RefeicaoForm(request.POST, instance=refeicao)
        if form.is_valid():
            form.save()
            return redirect('refeicoes:list_refeicoes')
    form = RefeicaoForm(instance=refeicao)
    context['form'] = form
    return render(request, template_name, context)

def delete_refeicao(request, id_refeicao):
    refeicao = Refeicao.objects.get(id=id_refeicao)
    refeicao.delete()
    return redirect('refeicoes:list_refeicoes')
