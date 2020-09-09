from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *

hora = timezone.now().hour - 3
nome = ''
logado = False
info = None

def setLogado(request):
    global logado
    logado = not logado

def login(request):
    global logado
    logado = False
    return render(request, 'login.html', {})

def validacao(request):
    global logado, nome
    if not logado:
        login = request.POST["username"]
        senha = request.POST["pass"]
        usuarios = Usuario.objects.all()
        perms = Acessa.objects.all()
        for user in usuarios:
            if login == user.matricula and senha == user.senha:
                setLogado(request)
                nome = user.nome
                for perm in perms:
                    if perm.usuario_id == user.id and perm.permissao == 'Administrador':
                        return redirect('index')
        else:
            return redirect('login')
    else:
        return redirect('login')

def erro(request):
    erro = 'É preciso o login para acessar esta página'
    return render(request, 'erro.html', {'erro': erro})

def index(request):
    global logado
    if logado:
        return render(request, 'index.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def animais(request):
    global logado
    if logado:
        return render(request, 'animais.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def estoque(request):
    global logado
    if logado:
        return render(request, 'estoque.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def gestacao(request):
    global logado
    if logado:
        return render(request, 'gestacao.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def produc_leite(request):
    global logado
    if logado:
        return render(request, 'produc_leite.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})


def graficos(request):
    global logado
    if logado:
        return render(request, 'graficos.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def modelos(dados, mod, acao):
    if acao:
        m = {
            'M': Material(tipo=dados[0], nome=dados[1], validade=dados[2], quantidade=dados[3]),
            'A': Animal(codigo=dados[0], nome=dados[1], sexo=dados[2], peso=dados[3])
            }
        return m[mod]
    else:
        if mod == 'M':
            return Material.objects.get(nome=dados)
        elif mod == 'A':
            return Animal.objects.get(codigo=dados)
        else:
            return ''

def adicionar(request):
    global logado
    if logado:
        dados = []
        for i in request.POST:
            if not i == 'modelo':
                dados.append(request.POST[i])
        aux = modelos(dados, request.POST['modelo'], True)
        aux.save()
        return HttpResponse('')
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def apagar(request):
    global logado
    if logado:
        aux = modelos(request.POST['codigo'], request.POST['modelo'], False)
        aux.delete()
        return HttpResponse('')
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

# ------ Funções da página Animal ------

def carregar_animais(request):
    global logado
    if logado:
        animais = Animal.objects.all()
        dados = []
        for animal in animais:
            dados.append(
                [
                    animal.codigo,
                    animal.nome,
                    animal.sexo,
                    animal.peso,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def info_animais(request):
    global logado, info
    if logado:
        codigo = request.POST['codigo']
        info = codigo
        return HttpResponse('')
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def carregar_info_animal(request):
    global logado, info
    if logado:
        animal = Animal.objects.get(codigo=info)
        return render(request, 'info_animais.html', {'animal': animal, 'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

# ------ Funções da página Estoque ------

def carregar_estoque(request):
    global logado
    if logado:
        estoque = Material.objects.all()
        dados = []
        for material in estoque:
            dados.append(
                [
                    material.tipo,
                    material.nome,
                    material.validade,
                    material.quantidade,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})
  

# ------ Funções da página Gestação ------

def carregar_gestacao(request):
    global logado
    if logado:
        prev= ''
        terminou = 'Em andamento'
        gestacao = Gravidez.objects.all()
        dados = []
        for gravidez in gestacao:
            gravAnt = Gravidez.objects.filter(animal=gravidez.animal, inicio2__isnull=False)
            #nulo = Gravidez.objects.get(animal=gravidez.animal, inicio2__isnull=True).inicio2
            #print(nulo)
            tempo = 283
            quant = 0
            dur = 0
            for ant in gravAnt:
                if not gravidez.inicio == ant.inicio:
                    quant+=1
                    ini = str(ant.inicio).split('-')
                    inid = int(ini[2])
                    inim = int(ini[1])
                    inia = int(ini[0])
                    ini = inid + (inim*30) + (inia*365)
                    fim = str(ant.inicio2).split('-')
                    fimd = int(fim[2])
                    fimm = int(fim[1])
                    fima = int(fim[0])
                    fim = fimd + (fimm*30) + (fima*365)
                    dur+= fim-ini
            if not quant==0:
                tempo = int(dur/quant)
            aux = str(gravidez.inicio).split('-')
            dia = tempo+(int(aux[2]))
            mes = int(aux[1])
            ano = int(aux[0])
            if dia > 30:
                if dia%30==0:
                    mes+= (int(dia/30)-1)
                    dia= 30
                else:
                    mes+= int(dia/30)
                    dia-= (int(dia/30) * 30)
                if mes>12:
                    ano+=1
                    mes-=12
            aux2 = [dia, mes, ano]
            if mes == 2 and dia > 28:
                aux2[1]+=1
                aux2[0]=28
            if dia < 10:
                aux2[0] = '0' + str(aux2[0])
            if mes < 10:
                aux2[1] = '0' + str(aux2[1])
            inicio = '{}/{}/{}'.format(aux[2],aux[1],aux[0])
            prev = '{}/{}/{}'.format(aux2[0],aux2[1],aux2[2])
            if not gravidez.inicio2 == None:
                auxT = str(gravidez.inicio2).split('-')
                if int(auxT[1]) == 2 and int(auxT[0]) > 28:
                    auxT[1] = '0' + str(int(auxT[1])+1)
                    aux2[0] = 28
                prev = '{}/{}/{}'.format(auxT[2],auxT[1],auxT[0])
                terminou = 'Terminada'
            else:
                terminou = 'Em andamento'
            dados.append(
                [
                    gravidez.id,
                    gravidez.animal.nome,
                    inicio,
                    terminou,
                    prev,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

# ------ Funções da página Produção de Leite ------

def carregar_produc_leite(request):
    global logado
    if logado:
        femeas = Animal.objects.filter(sexo = "Feminino")
        dados = []
        for femea in femeas:
            aux = Produc_leite.objects.get(femea = femea, data = request.GET['data'])
            dados.append(
                [
                    femea.codigo,
                    femea.nome,
                    aux.quantidade,
                    request.GET['data'],
                    ''
                ]
            )
        resposta = {"data":dados}
            return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

def get_femeas(request):
    if logado:
        femeas = Animal.objects.filter(sexo = "Feminino")
        lista_femeas = []
        for femea in femeas:
            lista_femeas.append(femea.nome)
        dados = {"lista_femeas":lista_femeas}
        return JsonResponse(dados)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

        

def dados_produc_leite(request):
    global logado
    if logado:
        animais = Animal.objects.filter(sexo='Feminino')
        dados = []

        nome = request.GET['codigo']
        hoje = datetime.now
        antes = datetime.timedelta(days=-7)
        produc_leite = []
        if nome == 'Geral':
            produc_leite = Produc_leite.objects.filter(data__range=(antes, hoje)).annotate(Count('data', distinct=True))
        else:
            animal = Animal.objects.get(nome=nome)
            produc_leite = Produc_leite.objects.filter(femea=animal, data__range=(antes, hoje))
            
        dados = {"produc_leite":produc_leite}
        return JsonResponse(dados)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'erro.html', {'erro': erro})

