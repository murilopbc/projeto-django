from django.shortcuts import render
from .models import Pessoas

def abrir_index(request):
    return render(request, 'index.html')

def listar_dados(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if Pessoas.objects.filter(nome=nome).exists():
            mensagem = 'Este nome já está cadastrado.'
        else:

            gravarCadastro = Pessoas(
                nome=nome,
                idade=idade
            )
            gravarCadastro.save()

            mensagem = (f'Dados do formulário: {nome} {idade}')
            
    dados = Pessoas.objects.all()
    
    return render(request, 'index.html', {'mensagem': mensagem, 'dados': dados, 'nome': nome, 'idade': idade})

