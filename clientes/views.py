from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,View,UpdateView
from django.urls import reverse_lazy #O reverse_lazy redireciona para uma pagina
from .models import Cliente
from .forms import ClienteForm #Importa a classe do arquivo form.py
# Create your views here.
class Home(ListView):
    def get(self,request):
        return render(request, 'clientes/homepage.html')


def series(request):
    return render(request, 'clientes/series.html')

def filmes(request):
    return render(request, 'clientes/filmes.html')

def lancamentos(request):
    return render(request, 'clientes/lancamentos.html')

class Cadastro(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cadastro.html'   #Gera o template do formulario
    def get_context_data(self, **kwargs):
        #**kwargs - espera qualquer argumento

        #Cria o context

        context = super().get_context_data(**kwargs) 
        context['titulo'] = 'Cadastro'
        context['botao'] = 'Cadastrar'
        return context
    success_url = reverse_lazy('login')


class BuscaCliente(View):
    def get(self, request): 
        return render(request , 'clientes/login.html') 


    def post(self,request):
        email=request.POST.get('email')
        senha = request.POST.get('senha')

        if email and senha:
            nosso_cliente = Cliente.objects.filter(email=email, senha=senha).first()
            if nosso_cliente:

                #Vamos criar as sessoes
                request.session['cliente_id'] = nosso_cliente.id
                request.session['nome_cliente'] = nosso_cliente.nome
                request.session['sobrenome_cliente'] = nosso_cliente.sobrenome
                request.session['cpf_cliente'] = nosso_cliente.cpf
                request.session["data_nascimento"] = nosso_cliente.data_nascimento.strftime("%d/%m/%Y")
                request.session['telefone_cliente'] = nosso_cliente.telefone
                request.session['email_cliente'] = nosso_cliente.email
                titulo = 'Cliente encontrado'
                return render(request, 'clientes/homepage.html',{'cliente': nosso_cliente, 'title':titulo})
            else:
                erro_message = "Nenhum cliente encontrado"
                return render(request, 'clientes/login.html',{'mensagem':erro_message})

        else:
            erro_message = "Por favor, informe um email e cpf para consulta"
            return render(request, 'clientes/login.html',{'mensagem':erro_message})
            
#Classe que encerra a sessão
class Logout(View):
    #Metodo que verifica e encerra a sessão
    def get (self,request):
        if 'nome_cliente' in request.session:
            del request.session['nome_cliente']
        if 'sobrenome_cliente' in request.session:
            del request.session['sobrenome_cliente']
        
        erro_message = 'Você foi desconectado'
        return render(request, 'clientes/login.html',{'mensagem':erro_message})
    

class Listagem(ListView):
    #a ferramenta listview permite (model,template_name)
    model = Cliente #Conecta ao modelo de banco de dados, E Retorna uma lista chamamda cliente_list 
    def get(self,request,*args,**kwargs):
        #Verificar se a sessão tem 'nome_cliente'
        if 'nome_cliente' not in request.session:
            return redirect('login')  
        #Se a sessao existir e o usuario 
        return super().get(request, *args, **kwargs)
    template_name = 'clientes/informacao.html'#Conecta ao arquivo html do templates
    context_object_name = 'clientes'

class Editar(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cadastro.html'   
    
    #Deixa dinamico dados no html
    def get_context_data(self, **kwargs):
        #**kwargs - espera qualquer argumento
        context = super().get_context_data(**kwargs) #Cria o context
        context['titulo'] = 'Edição dos Clientes'
        context['botao'] = 'Editar'
        return context
    
    # Atualiza a sessão com os novos dados
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
                
        cliente = form.instance
        self.request.session['cliente_id'] = cliente.id
        self.request.session['nome_cliente'] = cliente.nome
        self.request.session['sobrenome_cliente'] = cliente.sobrenome
        self.request.session['cpf_cliente'] = cliente.cpf
        self.request.session["data_nascimento"] = cliente.data_nascimento.strftime("%d/%m/%Y")  
        self.request.session['telefone_cliente'] = cliente.telefone
        self.request.session['email_cliente'] = cliente.email

        return response
    success_url = reverse_lazy('informacao')