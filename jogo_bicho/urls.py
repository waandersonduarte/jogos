
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('escolher_jogo', views.escolher_jogo, name='escolher_jogo'),
    path('mega_sena', views.mega_sena, name='mega_sena'),
    path('jogo_do_bicho', views.jogo_bicho, name='jogo_bicho'),
    path('resultados', views.resultados, name='resultados'),
    path('<int:jogo_bicho_id>', views.ver_sorteio, name='ver_sorteio'),
    #login
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
    path('cadastro', views.cadastro, name='cadastro'),

]