from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercicio
from rest_framework import viewsets
from .serializers import ExercicioSerializer
from .forms import ExercicioForm

# Create your views here.
class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer  

def add_exercicio(request):
    template_name = 'exercicios/add_exercicio.html'
    context = {}
    if request.method == 'POST':
        form = ExercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercicios:list_exercicios')
    else:
        form = ExercicioForm()
    context['form'] = form
    return render(request, template_name, context)

def list_exercicios(request):
    template_name = 'exercicios/list_exercicios.html'
    exercicios = Exercicio.objects.all()
    context = {
        'exercicios': exercicios,
    }
    return render(request, template_name, context)

def edit_exercicio(request, id_exercicio):
    template_name = 'exercicios/add_exercicio.html'
    context = {}
    exercicio = get_object_or_404(Exercicio, id=id_exercicio)
    
    if request.method == 'POST':
        form = ExercicioForm(request.POST, instance=exercicio)
        if form.is_valid():
            form.save()
            return redirect('exercicios:list_exercicios')
    else:
        form = ExercicioForm(instance=exercicio)
        
    context['form'] = form
    return render(request, template_name, context)

def delete_exercicio(request, id_exercicio):
    exercicio = get_object_or_404(Exercicio, id=id_exercicio)
    exercicio.delete()
    return redirect('exercicios:list_exercicios')