"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from clientes.views import Home,series,filmes,lancamentos,Cadastro,BuscaCliente,Logout,Listagem,Editar
=======
from clientes.views import Home,series,filmes,lancamentos,login,Cadastro,BuscaCliente,Logout,Listagem,Editar
>>>>>>> 56b34b9c3c2335268f9b302af870933d4f3920a0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='inicio'),
    path('series/', series, name='series'),
    path('filmes/', filmes, name='filmes'),
    path('lancamentos/', lancamentos, name='lancamentos'),
    path('login/', BuscaCliente.as_view(), name='login'),
    path('cadastro/', Cadastro.as_view(), name="cadastro"),
    path('sair/',Logout.as_view(), name='cliente_sair'),
    path('cliente_informacao/', Listagem.as_view(), name="informacao"),
    path('cliente_editar/<int:pk>', Editar.as_view(), name="cliente_update"),
]
