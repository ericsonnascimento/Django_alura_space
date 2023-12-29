from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroFroms
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{usuario} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválido!')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroFroms()

    if request.method == 'POST':
        form = CadastroFroms(request.POST)

        if form.is_valid():
            if form['senha'].value() != form['repete_senha'].value():
                messages.error(request, 'Senhas digitadas não são iguais!')
                return redirect('cadastro')

            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já cadastrado!')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})
