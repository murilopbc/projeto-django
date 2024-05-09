from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
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


def excluir_dados(request, id):
    pessoa  = get_object_or_404(Pessoas, id=id)
    print(pessoa)
    pessoa.delete()
    return abrir_index(request)

def abrir_edicao(request, id):
    pessoas = Pessoas.objects.filter(id=id)
    nome = pessoas[0].nome
    idade = pessoas[0].idade
    return render(request , 'cadastro.html',{"pessoas":pessoas,"nome":nome,"idade":idade,"id":id} )


def editar_dados(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    id = request.POST.get('id')

    pessoa = get_object_or_404(Pessoas ,id=id)

    pessoa.nome = nome
    pessoa.idade = idade
    
    pessoa.save()     
    return render (request, 'index.html')
    