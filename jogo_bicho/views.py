from multiprocessing import context
from django.shortcuts import render, redirect

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

def index(request):
    lista = JogoBicho.objects.all()
    hora = strftime('%H: %M: %S')
    context = {'hora': hora}
    return render(request, 'jogo_bicho/index.html',context)


def escolher_jogo(request):
    return render(request, 'jogo_bicho/escolher_jogo.html',{})

def mega_sena(request):
    return render(request, 'jogo_bicho/mega_sena.html', {})

def jogo_bicho(request, self, form):
    post = self.get_object()
    bicho = JogoBicho(**form.cleaned_data)
    bicho.jogo_bicho = post

    # if self.request.user.is_authenticated:
    #     bicho.usuario_comentario = self.request.user
        
    bicho.save()
    messages.success(self.request, 'Comentário enviado com sucesso.')
    return redirect('jogo_bicho/index.html', pk=post.id)
    

def mega_sena(request):
    if request.method == "POST":
        form = MegaSenaForm(request.POST, request.FILES)
        if form.is_valid():
            #bicho = form.save(commit=False)
            form.save()
            #return redirect('detalhar_livro', id=livro.id)
    else:
        form = MegaSenaForm()
    return render(request, 'mega_sena/mega_sena.html', {'form': form})

def resultados(request):
    #return render(request, 'jogo_bicho/index.html',{})
    hora = datetime.date.today()
    