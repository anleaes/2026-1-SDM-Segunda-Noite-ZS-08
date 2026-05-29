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


    def add_refeicao(self, request):
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