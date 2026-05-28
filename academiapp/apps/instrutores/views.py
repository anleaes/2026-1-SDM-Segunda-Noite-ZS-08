from django.shortcuts import render, get_object_or_404, redirect
from .models import Instrutor
from rest_framework import viewsets
from .serializer import InstrutorSerializer
from .forms import InstrutorForm

# Create your views here.
class InstrutorViewSet (viewsets.ModelViewSet):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer

def add_instrutor(request):
    template_name = 'instrutores/add_instrutor.html'
    context = {}
    if request.method == 'POST':
        form = InstrutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instrutores:list_instrutores')
    form = InstrutorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_instrutores(request):
    template_name = 'instrutores/list_instrutores.html'
    instrutores = Instrutor.objects.all()
    context = {
        'instrutores': instrutores,
    }
    return render(request, template_name, context)

def edit_instrutor(request, id_instrutor):
    template_name = 'instrutores/add_instrutor.html'
    context = {}
    instrutor = get_object_or_404(Instrutor, id=id_instrutor)
    if request.method == 'POST':
        form = InstrutorForm(request.POST, instance=instrutor)
        if form.is_valid():
            form.save()
            return redirect('instrutores:list_instrutores')
    form = InstrutorForm(instance=instrutor)
    context['form'] = form
    return render(request, template_name, context)

def delete_instrutor(request, id_instrutor):
    instrutor = Instrutor.objects.get(id=id_instrutor)
    instrutor.delete()
    return redirect('instrutores:list_instrutores')