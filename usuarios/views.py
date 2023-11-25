from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroFroms

# Create your views here.
def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroFroms()
    return render(request, 'usuarios/cadastro.html', {'form': form})