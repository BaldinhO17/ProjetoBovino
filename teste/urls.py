from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('validacao', views.validacao, name='validacao'),
    path('erro/', views.erro, name='erro'),
    path('inicio/', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('apagar/', views.apagar, name='apagar'),
    path('animais/', views.animais, name='animais'),
    path('animais/carregar/', views.carregar_animais, name='carregar_animais'),
    path('animais/info/', views.info_animais, name='info_animais'),
    path('animais/info-animal/', views.carregar_info_animal, name='carregar_info_animal'),
    path('estoque/', views.estoque, name='estoque'),
    path('estoque/carregar/', views.carregar_estoque, name='carregar_estoque'),
    path('gestacao/', views.gestacao, name='gestacao'),
    path('gestacao/carregar/', views.carregar_gestacao, name='carregar_gestacao'),
    path('graficos/', views.graficos, name='graficos'),
    path('graficos/get-femeas', views.get_femeas, name='get_femeas'),
    path('graficos/produc-leite/', views.dados_produc_leite, name='dados_produc_leite')
    

    
]
