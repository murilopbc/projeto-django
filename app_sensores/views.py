from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Pessoas

def abrir_index(request):
    dados = Pessoas.objects.all()
    return render(request, 'index.html', {'dados': dados})

def listar_dados(request):
    dados = Pessoas.objects.all()   
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    
    if Pessoas.objects.filter(nome=nome).exists():
        mensagem = 'Este nome já está cadastrado.' 
        return render(request, 'index.html', {'mensagem': mensagem,'dados': dados})
    else:

        gravarCadastro = Pessoas(
            nome=nome,
            idade=idade
        )
        gravarCadastro.save()

        mensagem = (f'Dados do formulário: {nome} {idade}')
         
    return render(request, 'index.html', {'mensagem': mensagem,'dados': dados})


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
    return redirect ('/')
    