
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('escolher_jogo', views.escolher_jogo, name='escolher_jogo'),
    path('mega_sena', views.mega_sena, name='mega_sena'),
    path('jogo_do_bicho', views.jogo_bicho, name='jogo_bicho'),
    path('mega_sena', views.mega_sena, name='mega_sena'),
    path('resultados', views.resultados, name='resultados'),

]