from django.contrib import admin

# Register your models here.
# clientes/admin.py
from django.contrib import admin
from .models import Cliente # Importa o modelo Cliente que você acabou de criar

# Registra o modelo Cliente no painel administrativo do Django
admin.site.register(Cliente)