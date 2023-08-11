from django.urls import path
from app_biografia import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # rota, view responsável, nome de referência

    #Rota Biografia(devdouglas.com)
    path('', views.home, name='home'),

    #Rota contatos (devdouglas.com/contatos)
    path('contatos/', views.contatos, name= 'lista_contatos'),

    #Rota curriculo (devdouglas.com/curriculo)
    path('curriculo/', views.curriculo, name='curriculo'),

]

