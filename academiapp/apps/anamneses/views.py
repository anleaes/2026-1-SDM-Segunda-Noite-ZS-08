from django.shortcuts import render, get_object_or_404, redirect
from .models import Anamnese
from rest_framework import viewsets
from .serializer import AnamneseSerializer
from .forms import AnamneseForm

# Create your views here.
class AnamneseViewSet (viewsets.ModelViewSet):
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer

def add_anamnese(request):
    template_name = 'anamnese/add_anamnese.html'
    context = {}
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anamnese:list_anamneses')
    form = AnamneseForm()
    context['form'] = form
    return render(request, template_name, context)

def list_anamneses(request):
    template_name = 'anamnese/list_anamneses.html'
    anamneses = Anamnese.objects.all()
    context = {
        'anamneses': anamneses,
    }
    return render(request, template_name, context)

def edit_anamnese(request, id_anamnese):
    template_name = 'anamnese/add_anamnese.html'
    context = {}
    anamnese = get_object_or_404(Anamnese, id=id_anamnese)
    if request.method == 'POST':
        form = AnamneseForm(request.POST, instance=anamnese)
        if form.is_valid():
            form.save()
            return redirect('anamnese:list_anamneses')
    form = AnamneseForm(instance=anamnese)
    context['form'] = form
    return render(request, template_name, context)

def delete_anamnese(request, id_anamnese):
    anamnese = Anamnese.objects.get(id=id_anamnese)
    anamnese.delete()
    return redirect('anamnese:list_anamneses')