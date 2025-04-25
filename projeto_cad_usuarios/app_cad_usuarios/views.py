from django.shortcuts import render
from .models import Usuario

# VIEWS BUSCA O CODIGO NECESSARIO PARA RENDERIZAR A PAGINA HTML
# request = lê informaçoes que estão vindo da pagina
# render = renderiza as informaçoes da pagina
#  ver informaçoes da pasta usuarios, pasta HTML home

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    # Extrair as informaçoes da tela, e colocalas em um novo usuario:
    # Pegando as informaçoes ja descritas no arquivo HTML, nome e idade do imput
    # Guardando as informaçoes em uma variavel
    # Salvar os dados da tela, para o banco de dados
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os usuarios já cadastrados em uma nova página

    usuarios = {
        #Retornando todos os usuarios que estao no banco de dados
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuarios
    return render(request,'usuarios/usuarios.html', usuarios)