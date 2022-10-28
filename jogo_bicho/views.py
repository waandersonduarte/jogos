from multiprocessing import context
from re import M
from django.shortcuts import render, redirect, get_object_or_404

from jogo_bicho.forms import JogoBichoForm
from jogo_bicho.models import JogoBicho
from mega_sena.forms import MegaSenaForm
import datetime
from time import sleep, strftime
from tkinter import *
from django.contrib import messages
from django.http import Http404
from django.db.models import Q, Count, Case, When
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.contrib.auth.models import User


def index(request):
    lista = JogoBicho.objects.all()
    hora = strftime('%H: %M')
    context = {'hora': hora, 'lista': lista}
    return render(request, 'jogo_bicho/index.html',context)


def escolher_jogo(request):
    return render(request, 'jogo_bicho/escolher_jogo.html',{})

def mega_sena(request):
    return render(request, 'jogo_bicho/mega_sena.html', {})

def jogo_bicho(request):
    if request.method != 'POST':
        form = JogoBichoForm()
        return render(request, 'jogo_bicho/jogo_bicho.html', {'form': form})

    form = JogoBichoForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = JogoBichoForm(request.POST)
        return render(request, 'jogo_bicho/jogo_bicho.html', {'form': form})

    bicho = request.POST.get('bicho')



    if not bicho:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'jogo_bicho/jogo_bicho.html')

    form.save()
    messages.success(request, 'Sorteio registrado com sucesso!')
    return redirect('jogo_bicho')


    

def mega_sena(request):
    if request.method != 'POST':
        form = MegaSenaForm()
        return render(request, 'mega_sena/mega_sena.html', {'form': form})

    form = MegaSenaForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = MegaSenaForm(request.POST)
        return render(request, 'mega_sena/mega_sena.html', {'form': form})

    num_1 = request.POST.get('num_1')
    num_2 = request.POST.get('num_2')
    num_3 = request.POST.get('num_3')
    num_4 = request.POST.get('num_4')
    num_5 = request.POST.get('num_5')
    num_6 = request.POST.get('num_6')

    if not num_1 or not num_2 or not num_3 or not num_4 or not num_5 or not num_6:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'mega_sena/mega_sena.html')

    form.save()
    messages.success(request, 'Sorteio registrado com sucesso!')
    return redirect('mega_sena')
    
def resultados(request):
    #return render(request, 'jogo_bicho/index.html',{})
    hora = datetime.date.today()

def ver_sorteio (request, jogo_bicho_id):
    #jogo_bicho = JogoBicho.objects.get(id=jogo_bicho_id)
    jogo_bicho = get_object_or_404(JogoBicho, id=jogo_bicho_id)

    # if not jogo_bicho.mostrar:
    #     raise Http404()

    return render(request, 'jogo_bicho/jogo_bicho.html', {
        'jogo_bicho': jogo_bicho
    })


def logout_usuario(request):
    logout(request)
    return render(request, 'jogo_bicho/login.html',{})
    
def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'jogo_bicho/escolher_jogo.html', {})
        
    else:
        return render(request, 'jogo_bicho/login.html',{})

def page_login(request):
    return render(request, 'jogo_bicho/login.html',{})


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'jogo_bicho/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')


    if not nome or not sobrenome or not email or not usuario or not senha \
             or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'jogo_bicho/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'jogo_bicho/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'jogo_bicho/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'jogo_bicho/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não confere.')
        return render(request, 'jogo_bicho/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'jogo_bicho/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe.')
        return render(request, 'jogo_bicho/cadastro.html')

    messages.success(request, 'Registrado com sucesso! Agora clique em Entrar.')                         

    user = User.objects.create_user(username=usuario, email=email, 
                                    password=senha, first_name=nome, 
                                    last_name=sobrenome)
    user.save()
    return redirect('cadastro')
    