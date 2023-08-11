from django.shortcuts import render, redirect
from .models import Contato

def home(request):
    return render(request, 'biografia/home.html')

def contatos(request):
    #Salvar os dados da tela para o banco de dados
    novo_contato = Contato()
    novo_contato.Nome = request.POST.get('Nome')
    novo_contato.Email = request.POST.get('Email')
    novo_contato.Telefone = request.POST.get('Telefone')
    novo_contato.save()

    return render(request, 'biografia/home.html')

    #porhora, a página de contatos estará em off
    # Exibir todos os contatos em uma nova página
    #contatos = {
     #   'contatos' : Contato.objects.all()
    #}
    
    #Retornar uma página com a lista de contatos
    #return render(request, 'biografia/contatos.html', contatos)

def curriculo(request):
    return render(request, 'biografia/curriculo.html')